# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:31:14 2019
@author: Adlla Katarine
"""

import tweepy
import re
import DynamoDBPut as ddb
dynamodb = ddb.DynamoDBPut()
import SentimentsAnalysisTweets as sat
sentimentTweets = sat.WatsonSentimentsAnalysis()

class CrawlerTwitter:
    __key = ''
    __keySecret = ''
    __token = ''
    __tokenSecret = ''
    __autentica = None
    __listJson = {}
    __listNameMovies = []
    __sentiment = False
    
    def __init__(self):
        self.__autentica = tweepy.OAuthHandler(self.__key, self.__keySecret)
        self.__autentica.set_access_token(self.__token, self.__tokenSecret)
    
    def readJson(self):
        for movies in dynamodb.getNameMovies():
            if movies != None:
                self.__listNameMovies.append(movies['title'])
        
    def tweetStream(self):
        ct_streamListener = CrawlerTwitterSL()
        api = tweepy.API(self.__autentica)
        stream = tweepy.Stream(api.auth, ct_streamListener)
        stream.filter(track= self.__listNameMovies, languages=["pt"])

class CrawlerTwitterSL(tweepy.StreamListener):

    def on_status(self, status):
        if not status.retweeted and 'RT @' not in status.text:
            for title in self.__listNameMovies:
                result = re.search(title, status.text)
                if(result.group(0) == title):
                    self.__sentiment = sentimentTweets.checkSentiment(status.text)
                    dynamodb.attSentiments(title, self.__sentiment)
                    break

    def on_error(self, status_code):
        if status_code == 420: 
            print('420 error')
            return False
        
if __name__ == '__main__':
    ct = CrawlerTwitter()
    ct.readJson()
    ct.tweetStream()
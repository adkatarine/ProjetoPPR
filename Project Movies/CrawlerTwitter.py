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
    __listNameMovies = []
    
    def __init__(self):
        self.__autentica = tweepy.OAuthHandler(self.__key, self.__keySecret)
        self.__autentica.set_access_token(self.__token, self.__tokenSecret)
    
    def readJson(self):
        result = dynamodb.getNameMovies()
        print(result)
        for movies in result:
            if movies != None:
                self.__listNameMovies.append(movies['title'])
        
    def tweetStream(self):
        ct_streamListener = CrawlerTwitterSL()
        ct_streamListener.getListNameMovies(self.__listNameMovies)
        api = tweepy.API(self.__autentica)
        stream = tweepy.Stream(api.auth, ct_streamListener)
        stream.filter(track= self.__listNameMovies, languages=["pt"])

class CrawlerTwitterSL(tweepy.StreamListener):
    __listNameMovies = []

    def on_status(self, status):
        print("***************************************")
        print(status.text)
        print("***************************************")
        if not status.retweeted and 'RT @' not in status.text:
            for title in self.__listNameMovies:
                result = re.search(title, status.text)
                if(result != None):
                    if(result.group(0) == title):
                        print("************PASSOU PELO IF************")
                        self.__sentiment = sentimentTweets.checkSentiment(status.text)
                        print("************PASSOU PELO MEIO DO IF************")
                        dynamodb.attSentiments(title, self.__sentiment)
                        break
            
    def on_error(self, status_code):
        if status_code == 420: 
            print('420 error')
            return False
    
    def getListNameMovies(self, listMovies):
        self.__listNameMovies = listMovies
    
if __name__ == '__main__':
    ct = CrawlerTwitter()
    ct.readJson()
    ct.tweetStream()
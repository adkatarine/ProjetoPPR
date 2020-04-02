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
    __key = 'sMdqkQ2LCZCy9QEzChQ3wQG5e'
    __keySecret = 'B2uPY7JEzbim7fiz1mPi6nKsrdtNxt44dDNOzNjNCyViE52kfF'
    __token = '1192966006215520257-XSvhiGrUBDLKvgjE1dRgG1t6bbmNJY'
    __tokenSecret = 'N5SrG3qLvZo1e62Ait41ArTM07oopAl8iBU03F4dB0paJ'
    
    def __init__(self):
        self.__autentica = tweepy.OAuthHandler(self.__key, self.__keySecret)
        self.__autentica.set_access_token(self.__token, self.__tokenSecret)
        self.__listNameMovies = []
    
    def getTitleMoviesDynamodb(self):
        nameMovies = dynamodb.getNameMovies()
        for movies in nameMovies:
            if movies != None:
                self.__listNameMovies.append(movies['title'])
        
    def tweetStream(self):
        ct_streamListener = CrawlerTwitterSL()
        ct_streamListener.setListNameMovies(self.__listNameMovies)
        api = tweepy.API(self.__autentica)
        stream = tweepy.Stream(api.auth, ct_streamListener)
        stream.filter(track= self.__listNameMovies, languages=["pt"])

class CrawlerTwitterSL(tweepy.StreamListener):
    __listNameMovies = []

    def on_status(self, status):
        if not status.retweeted and 'RT @' not in status.text:
            for title in self.__listNameMovies:
                result = re.search(title, status.text)
                if(result != None and len(status.text) > 10 and len((status.text).split(" "))):
                    if(result.group(0) == title):
                        self.__sentiment = sentimentTweets.checkSentiment(status.text)
                        dynamodb.attSentiments(title, self.__sentiment)
                        break
            
    def on_error(self, status_code):
        if status_code == 420: 
            print('420 error')
            return False
    
    def setListNameMovies(self, listMovies):
        self.__listNameMovies = listMovies
    
if __name__ == '__main__':
    ct = CrawlerTwitter()
    ct.getTitleMoviesDynamodb()
    ct.tweetStream()
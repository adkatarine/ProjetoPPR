# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:09:53 2020

@author: Adlla Katarine
"""

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, SentimentOptions

class WatsonSentimentsAnalysis:
    
    def __init__(self):
        self.__natural_language_understanding = NaturalLanguageUnderstandingV1(
          iam_apikey='',
          url='',
          version='2020-01-21')
    
    def checkSentiment(self, frase):
        self.__response = self.__natural_language_understanding.analyze(
          text=frase,
          language('pt'),
         features=Features(
        sentiment=SentimentOptions(document=True)
        ))
        return self.booleanSentiment(self.__response.get_result())
    
    def booleanSentiment(self, json):
        sentiments = json["sentiment"]["document"]["label"]
        if(sentiments == "positive"):
            return True
        else:
            return False

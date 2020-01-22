# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:09:53 2020

@author: Adlla Katarine
"""

#import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='',
  url='',
  version='2020-01-21')

response = natural_language_understanding.analyze(
  text='',
 features=Features(
entities=EntitiesOptions(
  emotion=False,
  sentiment=True,
  limit=1),
keywords=KeywordsOptions(
  emotion=False,
  sentiment=True,
  limit=1)))

#print(json.dumps(response, indent=2))
print(response.get_result())
print(response.get_headers())
print(response.get_status_code())
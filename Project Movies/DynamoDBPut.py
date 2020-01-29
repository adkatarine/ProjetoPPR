# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:32:19 2020

@author: Adlla Katarine
"""

import boto3

class DynamoDBPut:
    __dynamodb = boto3.resource('dynamodb')
    __dynamodbTable = __dynamodb.Table('Movies')

    def __init__(self):
        pass
        
    '''Adiciona um novo filme. '''
    def addMovies(self, title, sinopse, category, imageM):
        self.__dynamodbTable.put_Item(
            Item = {
                    'title': title,
                    'sinopse:': sinopse,
                    'category': category,
                    'imageM': imageM,
                    'positive': 0,
                    'negative': 0,
            },
            ConditionExpression = "attribute_not_exists(Id)"
        )
    
    '''Atualiza os sentimentos. '''
    def attSentiments(self, title, typeSentiment):
        if(typeSentiment == True):
            self.__dynamodbTable.update_item(
                Key={
                    'title': title,
                },
                UpdateExpression='SET positive = positive + :incr',
                ExpressionAttributeValues={
                    ':incr': 1
                }
            )
        else:
            self.__dynamodbTable.update_item(
                Key={
                    'title': title,
                },
                UpdateExpression='SET negative = negative + :incr',
                ExpressionAttributeValues={
                    ':incr': 1
                }
            )
    
    '''Pega o nome de cada filme'''
    def getNameMovies(self):
        response = self.__dynamodbTable.scan(
                AttributesToGet=[
                                'title',
                ],
        )
        return response['items']
    
    '''Apaga um filme a partir do título(chave primária). '''
    def deleteMovies(self, title):
        self.__dynamodbTable.delete_item(
                key={
                    'title': title,
                }
        )
    
    def checkMovieExist(self):
        pass
    
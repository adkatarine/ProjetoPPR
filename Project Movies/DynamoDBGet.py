# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 00:02:03 2020

@author: Adlla Katarine
"""

import boto3

class DynamoDBPut:
    __dynamodb = boto3.resource('dynamodb')
    __dynamodbTable = __dynamodb.Table('Movies')

    def __init__(self):
        pass
    
    '''Recupera todos os dados da tabela. '''
    def batchGetMovies(self):
        response = self.__dynamodbTable.scan()
        return response['Items']
    
    def returnJsonMovies(self, response):
        pass
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 00:02:03 2020

@author: Adlla Katarine
"""

import boto3

class DynamoDBGet:

    def __init__(self):
        __dynamodb = boto3.resource('dynamodb', aws_access_key_id='',
                                    aws_secret_access_key='', region_name='us-east-1')
        self.__dynamodbTable = __dynamodb.Table('Movies')
    
    '''Recupera todos os dados da tabela. '''
    def batchGetMovies(self):
        response = self.__dynamodbTable.scan()
        return response['Items']
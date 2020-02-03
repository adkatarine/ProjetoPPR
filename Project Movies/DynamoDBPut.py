# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:32:19 2020

@author: Adlla Katarine
"""

import boto3

class DynamoDBPut:

    def __init__(self):
        __dynamodb = boto3.resource('dynamodb', aws_access_key_id='',
                                aws_secret_access_key='', region_name='us-east-1')
        self.__dynamodbTable = __dynamodb.Table('Movies')
        
    '''Adiciona um novo filme. '''
    def addMovies(self, listMovies):
        newListMovies = self.checkMovieExist(listMovies)
        
        if(newListMovies != None):
            for dictMovie in newListMovies:
                self.__dynamodbTable.put_item(
                    Item = {
                            'title': dictMovie['title'],
                            'sinopse:': dictMovie['sinopse'],
                            'category': dictMovie['category'],
                            'imageM': dictMovie['imageM'],
                            'positive': 0,
                            'negative': 0,
                    },
                    ConditionExpression = "attribute_not_exists(Id)"
                )
        elif():
            print("****************NÃO HÁ DADOS PARA CADASTRAR!****************")
    
    '''Atualiza os sentimentos. '''
    def attSentiments(self, title, typeSentiment):
        if(typeSentiment == True):
            self.__dynamodbTable.update_item(
                Key={
                    'title': title
                },
                UpdateExpression='SET positive = positive + :incr',
                ExpressionAttributeValues={
                    ':incr': 1
                }
            )
        else:
            self.__dynamodbTable.update_item(
                Key={
                    'title': title
                },
                UpdateExpression='SET negative = negative + :incr',
                ExpressionAttributeValues={
                    ':incr': 1
                }
            )
    
    '''Pega o nome de cada filme. '''
    def getNameMovies(self):
        response = self.__dynamodbTable.scan(
                AttributesToGet=[
                                'title'
                ]
        )
        print("*************PASSOU POR GETNAMEMOVIE*************")
        print("*************PASSOU POR GETNAMEMOVIE*************")
        print("*************PASSOU POR GETNAMEMOVIE*************")
        print("*************PASSOU POR GETNAMEMOVIE*************")
        return response['Items']
    
    '''Apaga um filme a partir do título(chave primária). '''
    def deleteMovies(self, listTitles):
        for title in listTitles:
            self.__dynamodbTable.delete_item(
                    Key={
                        'title': title
                    }
            )
        print("*************PASSOU POR DELETEMOVIE*************")
        print("*************PASSOU POR DELETEMOVIE*************")
        print("*************PASSOU POR DELETEMOVIE*************")
        print("*************PASSOU POR DELETEMOVIE*************")
    
    '''Verifica se os filmes em cartaz ainda são os mesmos, atualizando a tabela com os estreados e apagando
    os que saíram de cartaz. '''
    def checkMovieExist(self, listMovies):
        listTitle = self.getNameMovies()
        
        if(listTitle != None):
            print("*************PASSOU PELO IF*************")
            print("*************PASSOU PELO IF*************")
            print("*************PASSOU PELO IF*************")
            print("*************PASSOU PELO IF*************")
            for dictMovie in listMovies:
                for title in listTitle:
                    if(dictMovie['title'] != None and title['title'] != None):
                        if(dictMovie['title'] == title['title']):
                            print("*************PASSOU PELO IF DE NOVO*************")
                            listTitle.remove(title)
                            listMovies.remove(dictMovie)
                self.deleteMovies(listTitle)
                print("*************ACABOU FUNÇÃO*************")
                print("*************ACABOU FUNÇÃO*************")
                print("*************ACABOU FUNÇÃO*************")
                print("*************ACABOU FUNÇÃO*************")
        return listMovies
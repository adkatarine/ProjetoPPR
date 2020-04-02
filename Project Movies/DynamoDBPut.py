import boto3

class DynamoDBPut:

    def __init__(self):
        __dynamodb = boto3.resource('dynamodb', aws_access_key_id='AKIAIQN25V2WBEFAZBGA',
                                    aws_secret_access_key='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', 
                                    region_name='us-east-1', endpoint_url = "http://dynamodb.us-east-1.amazonaws.com")
        self.__dynamodbTable = __dynamodb.Table('Movies')
        
    '''Adiciona um novo filme. '''
    def addMovies(self, listMovies):
        #newListMovies = self.checkMovieExist(listMovies)
        if(listMovies != None):
            for dictMovie in listMovies:
                if(dictMovie['title'] != None):
                    self.__dynamodbTable.put_item(
                        Item = {
                                'title': dictMovie['title'],
                                'sinopse:': dictMovie['sinopse'],
                                'category': dictMovie['category'],
                                'imageM': dictMovie['imageM'],
                                'positive': 0,
                                'negative': 0,
                        }
                    )
    
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
        return response['Items']
    
    '''Apaga um filme a partir do título(chave primária). '''
    def deleteMovies(self, listTitles):
        for title in listTitles:
            self.__dynamodbTable.delete_item(
                    Key={
                        'title': title['title']
                    }
            )
    
    '''Verifica se os filmes em cartaz ainda são os mesmos, atualizando a tabela com os estreados e apagando
    os que saíram de cartaz. '''
    def checkMovieExist(self, listMovies):
        listTitle = self.getNameMovies()
        
        if(listTitle != None and listMovies != None):
            for dictMovie in listMovies:
                for title in listTitle:
                    if(dictMovie['title'] != None):
                        if(dictMovie['title'] == title['title']):
                            listTitle.remove(title)
                            listMovies.remove(dictMovie)
            self.deleteMovies(listTitle)
        return listMovies
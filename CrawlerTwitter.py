# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:31:14 2019
@author: Adlla Katarine
"""
import tweepy
import Treatments as tm
treatments = tm.Treatments()
#import json

class CrawlerTwitter:
    __key = ''
    __keySecret = ''
    __token = ''
    __tokenSecret = ''
    __autentica = None
    __listJson = {}
    __listNameMovies = []
    
    def __init__(self):
        self.__autentica = tweepy.OAuthHandler(self.__key, self.__keySecret)
        self.__autentica.set_access_token(self.__token, self.__tokenSecret)
    
    def readJson(self):
        self.__listJson = treatments.readJson()
        self.__listNameMovies = treatments.nameMovies(self.__listJson['complet'])
        
    def tweetStream(self):
        ct_streamListener = CrawlerTwitterSL()
        api = tweepy.API(self.__autentica)
        #mv = [str(u) for u in self.__listNameMovies]
        #mv.remove('None')
        filme = ['Adam', 'Malévola - Dona do Mal', ' A Família Addams', 'bob esponja', 'O Exterminador do Futuro: Destino Sombrio',
              'Dora e a Cidade Perdida', 'patrick', 'Doutor Sono', 'Estaremos Sempre Juntos', 'Ford vs. Ferrari', 'As Panteras',
              'Invasão ao Serviço Secreto', 'Dora e a Cidade Perdida', 'Coringa']
        stream = tweepy.Stream(api.auth, ct_streamListener)
        stream.filter(track= filme, languages=["pt"])
        
    def getListNameMovies(self):
        return self.__listNameMovies
    
    def getAutentica(self):
        return self.__autenticas
    
    def getListJson(self):
        return self.__listJson
    
class CrawlerTwitterSL(tweepy.StreamListener):

    def on_status(self, status):
        if not status.retweeted and 'RT @' not in status.text:
            print('TWEET')
            #print(status.text)
            print([status.user.name,status.text])
            with open("tweetsCrawler.txt", 'a') as tf:
                tf.write(status.text)

    def on_error(self, status_code):
        if status_code == 420: 
            print('420 error')
            return False
        
    #def on_data(self, data):
    #    print(data)
      #  with open("tweetsCrawler.txt", 'a') as tf:
            #tf.write(data)
            #json_load = json.loads(data)
            #text = {'text': json_load['text'], }
            #tf.write(json.dumps(text))
       #     tf.write(data)
        
if __name__ == '__main__':
    ct = CrawlerTwitter()
    ct.readJson()
    ct.tweetStream()
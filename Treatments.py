# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:55:42 2019

@author: Adlla Katarine
"""
import json
import os.path

class Treatments:
    
    def writeJson(self, lista):
        with open("InformationsM.json", "w") as outfile:
            json.dump(self.informationsM, outfile, ensure_ascii = False)
        
    def readJson(self):
        with open("InformationsM.json", "r") as file:
            return json.load(file)
        
    def fileExist(self, file):
       if os.path.isfile(file) == True:
           return os.path.exists(file)
    
    def checkJsonEquals(self, auxJson1, auxJson2):
        return auxJson1 == auxJson2
        
    '''Verifica se um determinado filme já está adicionado na lista. Retorna boolean.'''
    def checkMovieList(self, lista, movie):
       return movie in lista
   
    def nameMovies(self, jsonL):
        listMovies = []
        for movies in jsonL:
            if movies != 'None': 
                listMovies.append(movies['name'])
        return listMovies
            
            
            
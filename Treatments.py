# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:55:42 2019

@author: Adlla Katarine
"""
import json
import os.path

class Treatments:
    __wordsPositive = ['encantado', 'encantada', 'encantador', 'legal', 'animado', 'animada', 'entusiasmado', 'entusiasmada',
                'amei', 'amo', 'feliz', 'bom', 'admirável', 'lindo', 'admirado', 'admirada', 'surpresa', 'surpreso',
                'alegre', 'agradável', 'adorei', 'adoro', 'divertido', 'prazeroso', 'prazerosa', 'adorável', 'maravilhoso',
                'melhor', 'perfeito', 'excelente', 'brilhante', 'extraordinário']

    __wordsNegative = ['raiva', 'desapontado', 'desapontada', 'irritado', 'irritada', 'ruim', 'péssimo', 'horrível', 
                 'odiei', 'odeio', 'irritante', 'arrependido', 'arrependida', 'desgosto', 'chato', 'detestável',
                 'insuportável', 'desagradável', 'decepção', 'decepcionado', 'decepcionou', 'decepcionada',
                 'pior', 'piorou']
    
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
   
    def description(self, jsonL):
        
    
    def nameMovies(self, jsonL):
        listMovies = []
        for movies in jsonL:
            if movies != 'None': 
                listMovies.append(movies['name'])
        return listMovies
            
    def checkPositiveOrNegative(self, description):
        quantP = 0
        quantN = 0
        description = description.split(' ', ',')
        for dtweet in description:
            if(dtweet in self.__wordsPositive):
                quantP += 1
            elif(dtweet in self.__wordsNegative):
                quantN += 1
            else:
                continue
        listPN = {'quantP': quantP, 'quantN': quantN}
        return listPN
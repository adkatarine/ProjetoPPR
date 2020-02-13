# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 02:16:58 2020

@author: Adlla Katarine
"""

from time import sleep
import subprocess

timeout = 60

while True:
    command = 'scrapy runspider CrawlerMovies.py'
    subprocess.run(command, shell=True)
    sleep(timeout)
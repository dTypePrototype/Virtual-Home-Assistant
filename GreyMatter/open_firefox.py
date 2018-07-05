#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:54:13 2018

@author: dewang
"""
from selenium import webdriver

from SenseCells.tts import tts

def open_firefox():
    tts('Affirmative Boss, Opening Firefox')
    webdriver.Firefox(executable_path='/home/dewang/Downloads/geckodriver-v0.21.0-linux64/geckodriver')
    


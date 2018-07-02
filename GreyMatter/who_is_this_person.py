#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 20:06:49 2018

@author: dewang
"""

import re

import wikipedia

from SenseCells.tts import tts

def who_is_this_person(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove('who')
    words_of_message.remove('is')
    cleaned_message = ' '.join(words_of_message)
    print(cleaned_message)
    try:
        wiki_data = wikipedia.summary(cleaned_message, sentences=5)
        
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(wiki_data)
        while m:
            wiki_data= m.group(1) + m.group(2)
            m = regEx.match(wiki_data)
        print(wiki_data)
        wiki_data = wiki_data.replace("'", "")
        tts(wiki_data)
    except wikipedia.exceptions.DisambiguationError as e:
        tts ('Can you please be more specific? You may choose something from the following.')
        print("Can you please be more specific? You may choose something from the following.; {0}".format(e))

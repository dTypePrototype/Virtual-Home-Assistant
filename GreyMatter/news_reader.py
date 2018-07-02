#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:08:16 2018

@author: dewang
"""

import requests
import re
from SenseCells.tts import tts




def news_reader():
    all_news_headlines=""
    api_url= 'https://newsapi.org/v2/top-headlines?country=in&apiKey=dee9308a4cb841c7926560f92d84799f'
    json_data = requests.get(api_url).json()
    for i in range(20):
        if json_data['articles'][i]['title'] == None:
            json_data['articles'][i]['title']=" "
        elif json_data['articles'][i]['description']== None:
            json_data['articles'][i]['description']=" "
        all_news_headlines=all_news_headlines+json_data['articles'][i]['title']+".\n"+json_data['articles'][i]['description']+"\n\n"
    
    regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
    m = regEx.match(all_news_headlines)
    while m:
        all_news_headlines= m.group(1) + m.group(2)
        m = regEx.match(all_news_headlines)
    all_news_headlines=all_news_headlines.replace("'", "")
    print(all_news_headlines)
    all_news_headlines=all_news_headlines.encode("utf-8")
    tts("Here are top news headlines:\n\n")
    tts(all_news_headlines)    
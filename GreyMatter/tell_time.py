#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:42:22 2018

@author: dewang
"""
from datetime import datetime

from SenseCells.tts import tts

def what_is_time():
    tts("The time is "+datetime.strftime(datetime.now(), '%H:%M:%S'))


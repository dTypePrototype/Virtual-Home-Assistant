# -*- coding: utf-8 -*-
import random
from SenseCells.tts import tts

def who_are_you():
    messages= ['I am your Personal Assistant.','Your Personal Assistant, didnt I told you before?','You ask that so many times! I am your Personal Assistant. ']
    tts(random.choice(messages))

def how_am_i():
    replies=['You are a person with good heart', 'You are a cute guy, sir','You are goddamn handsome!, I wish to take you home','You are sexy!','My knees go weak when I see you']
    tts(random.choice(replies))
    
def tell_joke():
    jokes = ['What do you get when you cross-breed a shark and a cow? I have no idea but I wouldn’t try milking it.','How can you tell you have a really bad case of acne? It’s when the blind try to read your face.','What happens to a frogs car when it breaks down? It gets toad away.', 'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.']
    tts(random.choice(jokes))  
    
def who_am_i(name):
    tts('You are Mister'+name+', an awesome computer techie and a music lover. I am happy to server you sir!')
    
def where_born():
    tts('I was created the young gentleman named Dewang, in the lovely city of Dehradun, in the foothills of Himalayas, in India.')

def how_are_you():
    fine=['I am fine, thank you very much.','I am fine today, glad you asked','I dont know, I guess a little polymorphic, slightly complex, or maybe a little stoned. Chill! I am all good.']
    tts(random.choice(fine))
    

def undefined():
    tts('I dont know what that means, Sir!') 
    
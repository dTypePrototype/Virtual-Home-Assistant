from GreyMatter import tell_time, general_conversations, weather, define_subject, who_is_this_person,news_reader, open_firefox, sleep, play_music
from GreyMatter.SenseCells.tts import tts
def brain(name, speech_text, music_path, city_name, city_code):
    def check_message(check):
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False
        
    if check_message(['who','are','you' ]):
        general_conversations.who_are_you()
        
    elif check_message(['how','i','look' ]) or check_message(['how','am','i']):
        general_conversations.how_am_i()
    
    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()
        
    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i(name)

    elif check_message(['where', 'born']):
        general_conversations.where_born()

    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()
        
    elif check_message(['party', 'time']) or check_message(['party', 'mix']):
        play_music.play_shuffle(music_path)
    
    elif check_message(['time']):
        tell_time.what_is_time()
        
    elif check_message(['weather']) or check_message(['hows', 'weather']):
        weather.weather(city_name, city_code)
        
    elif check_message(['define']):
        define_subject.define_subject(speech_text)
        
    elif check_message(['who','is']):
        who_is_this_person.who_is_this_person(speech_text)
        
    elif check_message(['headlines','news']):
        news_reader.news_reader()
        
    elif check_message(['open', 'firefox']):
        open_firefox.open_firefox()
        
    elif check_message(['sleep']):
        sleep.go_to_sleep()
        
    elif check_message(['play', 'music']) or check_message(['music']):
        play_music.play_random(music_path)
        
    elif check_message(['play']):
        play_music.play_specific_music(speech_text, music_path)
            
    else:
        general_conversations.undefined()
 
import requests
from SenseCells.tts import tts

def weather(city_name, city_code):
    api_address= 'http://api.openweathermap.org/data/2.5/weather?appid=60c9bd7f6a8da0632bd76ac138660b01&q='
    url = api_address+ city_name
    json_data = requests.get(url).json()
    discript = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    message= "It is "+str(discript)+" and "+str(int(temp-273))+" degree celcius in Dehradun"
    tts(message)
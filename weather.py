import requests
import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak('hello we are going to get weather of a city based on your choice')
speak('please tell you city name')

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    r.dynamic_energy_threshold=300
    r.pause_threshold = 0.8
    audio = r.listen(source)
print("Recognizing...")
try:
    city=r.recognize_google(audio)
except Exception as e:
    print(e)
print("User said: "+city)   
url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={create_your_appid on open weather map}&units=metric'.format(city)
res=requests.get(url)
data=res.json()


temp=data['main']['temp']
wind_speed=data['wind']['speed']

print("Temperature is "+format(temp)+" degree celsius")
print("wind speed is "+format(wind_speed)+" meters per second")
speak("Temperature is"+format(temp)+"degree celsius")
speak("wind speed is"+format(wind_speed)+"meters per second")

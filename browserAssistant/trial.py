import pyaudio  #for managing input and output audio stream
import speech_recognition as sr    #to convert speech to str
from selenium import webdriver     #framework to automate browser(downloaded edge driver)
from selenium.webdriver.common.keys import Keys
import pyttsx3      #to convert voice to str
import datetime
import subprocess
import webbrowser
import pywhatkit


engine = pyttsx3.init()
voices = engine.getProperty('voices')       #to get voices of both male and female
engine.setProperty('voice',voices[1].id)    #setProperty takes name of value and the value,    voices[0]=male, [1]=female
recognizer = sr.Recognizer()        #to recognize voice of user
mic = sr.Microphone()               #for microphone

inp=""
driver = webdriver.Edge()       
driver.maximize_window()        #when driver starts the window maximizes itself


def cmd():
    with mic as source:
        print("clearing background noices")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        audio = recognizer.listen(source)

    try:
        inp = recognizer.recognize_google(audio)        #google assistant so recognize_google and audio(user input from mic) and convert to input string
        print(inp)

    except:
        inp = "Error"


    return inp

# func to speak user input
def speak(str):

    engine.say(str)     #say func so assistant speak this text
    engine.runAndWait()         #to make sure it runs say func and wait to complete the text

while True:
    inp = cmd()
    if 'play' in inp:
        speak("playing...")
        pywhatkit.playonyt(inp)
        # driver.execute_script("window.open('');")
        # window_list = driver.window_handles #stores list of all tabs
        # driver.switch_to_window(window_list[-1])        #to switch to latest tab
        # driver.get('https://google.com')        #url of google

        
        # subprocess.Popen(["https://google.com"])

    elif 'time' in inp:
        time = datetime.datetime.now()
        print(time)
        speak(time)

    elif ('open google' in inp):
        speak("openning google...")

        driver.execute_script("window.open('');")

        window_list = driver.window_handles #stores list of all tabs

        driver.switch_to_window(window_list[-1])        #to switch to latest tab

        driver.get('https://google.com')        #url of google
        
    else:
        pass



# installed pyaudio speechRecognition selenium pyttsx3 bs4(beautifulsoup) 
import pyaudio  #for managing input and output audio stream
import speech_recognition as sr    #to convert speech to str
from selenium import webdriver     #framework to automate browser(downloaded edge driver)
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By #to import element
from selenium.webdriver.support.ui import WebDriverWait #to move in UI on any platform
import pyttsx3      #to convert voice to str
import time
import datetime
import pywhatkit
from bs4 import BeautifulSoup
import requests



driver = webdriver.Edge()       
#edge coz driver of edge downloaded, and taken location as args

driver.maximize_window()        #when driver starts the window maximizes itself
wait = WebDriverWait(driver,3)      #takes driver and ime to wait

# initializing voice assistant
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #to get voices of both male and female
engine.setProperty('voice',voices[1].id)    #setProperty takes name of value and the value,    voices[0]=male, [1]=female


recognizer = sr.Recognizer()        #to recognize voice of user
mic = sr.Microphone()               #for microphone



# .................................................................
# func to speak user input
def speak(str):

    engine.say(str)     #say func so assistant speak this text
    engine.runAndWait()         #to make sure it runs say func and wait to complete the text


# func to recognize user input
def recog():

    # using mic as source listen to mic for 8 sec to have user input
    with mic as source: 
        audio = recognizer.listen(source, phrase_time_limit=5)
        print("clearing background noices")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

    inp = ""        #user input string

    speak("identifying speech...")
    

    try:
        inp = recognizer.recognize_google(audio)        #google assistant so recognize_google and audio(user input from mic) and convert to input string

    except:
        inp = "Error"


    return inp



# func to open website
def open(inp,url):
            speak("openning"+inp)
            driver.execute_script("window.open('');")
            window_list = driver.window_handles #stores list of all tabs
            driver.switch_to.window(window_name=window_list[-1])       #to switch to latest tab
            driver.get(url) 

# func to search website
def search(elem):

    while True:         #until the search completes
        speak("searching...")

        inp = recog()         #getting query from user to search
        if(inp!="Error"):
            break
    
    element = driver.find_element('xpath','//*[@id="APjFqb"]')       #name of google search space
    element.clear()     #clear box
    element.send_keys(inp)    #search query
    element.send_keys(Keys.RETURN)  #enter to search

# start
# .........................................
platform = {"open google":"https://google.com", 
                "open youtube":"https://www.youtube.com", 
                "open youtube music":"https://music.youtube.com",
                "open get hub": "https://github.com",
                "open linkedin":"https://www.linkedin.com",
                "open whatsapp": "https://web.whatsapp.com"}

serches = {"search google":'//*[@id=\"APjFqb\"]', 
            "search youtube":'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input', 
            "search yt music":'//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/tp-yt-paper-icon-button[1]', 
            "search get hub": 'query-builder-test',
            "search linkedin":'global-nav-search'}
    
time.sleep(3)
speak("Hello, Your assistant is at you're service...")

while True:
    speak("How can I help you..?")
    

    # taking voice continuesly from user
    inp = recog().lower()     #returns user input as string
    print(inp)

    
    

# to open specific platforms
    if inp in platform:
        speak("opening...")
        open(inp, url=platform[inp])        #input and its url is as args

# to search on specific platforms
    elif inp in serches:
        speak("searching...")
        search(elem=serches[inp])   #no need to send inp, but elem is important
    
    # to open and play youtube directly
    elif 'play' in inp:
        speak("playing...")
        pywhatkit.playonyt(inp)

    # to get current system time
    elif 'time' in inp:
        print(time)
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        speak(time)

# to send message to specific person
    elif 'search youtube music' in inp:
        #  pywhatkit.sendwhatmsg("+919825018703", "Heloooooo", 10,30)
        searchbox = driver.find_element('xpath','//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/tp-yt-paper-icon-button[1]')
        # searchbox.send_keys('hanuman chalisa')
        searchbox.send_keys(Keys.RETURN)        
    
    
    # elif 'link' in inp:

        # linkNum = inp.split(' ')
        # num = linkNum[1]
        # print(num)
        
        # linkName = recog()
        
        # element = driver.find_element('xpath','//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3').click()
        # element = driver.find_element(By.LINK_TEXT, linkName).click

    elif 'move' in inp:
        
        ans = inp.split(' ')
        ans = ans[1]
        
        if(ans=='forward'):
             driver.forward()
        else:
             driver.back()

    elif 'refresh' in inp:
        speak("refreshing")
        driver.refresh()
         
    elif 'i quit' in inp:
         driver.quit()

    elif 'new' in inp:
         
        ans = inp.split(' ')
        ans = ans[1]

        if ans=='window':
            speak("opening window")
            driver.switch_to.new_window('window')
        else:
            speak("opening tab")
            driver.switch_to.new_window('tab')    

    elif 'close tab' in inp:
         driver.close()  

    elif 'minimise window' in inp:
         driver.minimize_window()

    elif 'maximize window' in inp:
         driver.maximize_window()

    elif 'full screen window' in inp:
         driver.fullscreen_window()

    else:
         pass


    
# func to search website
# def search(elem):

#     while True:         #until the search completes
#         speak("searching...")

#         inp = recog()         #getting query from user to search
#         if(inp!="Error"):
#             break
    
#     element = driver.find_element(By.ID, elem)      #name of google search space
#     element.clear()     #clear box
#     element.send_keys(inp)    #search query
#     element.send_keys(Keys.RETURN)  #enter to search
# ?.......................

# serches = {"search google":"q", 
#             "search youtube":"center", 
#             "search yt music":"icon", 
#             "search linkedin":"global-nav-search"}

# ..................


# elif inp in serches:
    #     speak("searching...")
    #     search(elem=serches[inp])   #no need to send inp, but elem is important

# ,.............


# if ('open google' in inp):
    #     speak("openning google...")

    #     driver.execute_script("window.open('');")

    #     window_list = driver.window_handles #stores list of all tabs

    #     driver.switch_to.window(window_name=window_list[-1])       #to switch to latest tab

    #     driver.get('https://google.com')        #url of google

    # elif ('search google' in inp):

    #     while True:
    #         speak("searching...")

    #         inp = recog()         #getting query from user to search
    #         if(inp!="Error"):
    #             break

    #     element = driver.find_element(By.NAME, "q")      #name of google search space
    #     element.clear()     #clear box
    #     element.send_keys(inp)    #search query
    #     element.send_keys(Keys.RETURN)  #enter to search
    
    
    # elif ('open youtube' in inp):
    #     speak("openning youtube...")

    #     driver.execute_script("window.open('');")

    #     window_list = driver.window_handles #stores list of all tabs

    #     driver.switch_to.window(window_name=window_list[-1])       #to switch to latest tab

    #     driver.get('https://www.youtube.com') 


    
    # elif 'play' in inp:
    #     speak("playing...")
    #     pywhatkit.playonyt(inp)

    # elif 'time' in inp:
    #     print(time)
    #     time = datetime.datetime.now()
    #     print(time)
    #     speak(time)

    # elif ('open youtube music' in inp):
    #     open(inp,"https://music.youtube.com")

    # else:
    #     pass

    # break
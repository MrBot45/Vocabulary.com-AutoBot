# -*- coding: utf-8 -*- 
__version__ = "1.2.4"
import os
import platform
from selenium import webdriver
import time
from unidecode import unidecode
import urllib2
import httplib
import json
import sys
import speech_recognition as sr
import audioop
import urllib
from update import update

from pydub import AudioSegment
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from os import path

_author_ = "Sayan Bhowmik and lefela4(Felix)"
fo = open('cred')
fo_ = open('voclist')
r = sr.Recognizer()

html = ''
skipAudio = 0
tries = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "excludeSwitches", ["ignore-certificate-errors"])
check_driver_version = 1
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_binary=binary, firefox_options = opts)
#====================================================================================================================================================#
login_page = "https://www.vocabulary.com/login/"
my_username = fo.readlines()[0]
fo.seek(0, 0)
my_pass = fo.readlines()[1]

############################################################################
# Link to  assignment [For Demo]
url = fo_.readlines()[0] #YOUR URL HERE
##############################################################################

print "Voc at " + url
a_page = url
lastAudioLen = 0

print "[+] STARTING VOCABULARY BOT"
usr = ""
base = ""
old_html = ""
source = ""
soup = ""
op1 = ""
op2 = ""
op3 = ""
op4 = ""
options = []
word = ""
#====================================================================================================================================================#


def main():
    '''
    # Ignore this section, I actually ended up making a keygen to protect it from the hands of students at my University

    ck = 0

     if(platform.system() == "Linux" or platform.system() == "Darwin" and len(key) >= 10 and ck == 0):
            base = platform.uname()[0][0]
            usr = platform.uname()[1][0]
            u = key[-2:][0]
            b = key[-2:][1]
            if(usr == u and base == b):
                            time.sleep(2)
                            login();
                            assignment();
                            ck += 1


    if(platform.system() == "Windows" and len(key) >= 10 and ck == 0):
            usr = os.getenv('username')[2]
            base = platform.uname()[0][0]

            u = key[-2:][0]
            b = key[-2:][1]
            if(usr == u and base == b):
    time.sleep(2)
    login();
    assignment();
    ck += 1
    '''
    time.sleep(2)
    login()
    assignment()

#====================================================================================================================================================#


def login():
    driver.get(login_page)
    time.sleep(3)
    print "Attemp to login in"
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys(my_username)
    password.send_keys(my_pass)
    driver.find_element_by_class_name("green").click()
    time.sleep(1)
    try:
        alertObj = driver.switch_to.alert
        alertObj.accept()
        print "Alert detected!"
        driver.get(url)
    except Exception as e:
        print("No alert found!")

#====================================================================================================================================================#
def assignment():
    try:
        alertObj = driver.switch_to.alert
        alertObj.accept()
        print "Alert detected!"
        driver.get(url)
    except Exception as e:
        print("No alert found!")
    time.sleep(3)
    driver.get(a_page)
    time.sleep(2)
    driver.execute_script("window.scrollTo(100, 100);")
    option_high_score = scrapper()
    click_op(option_high_score)
    print "[+] STARTING VOCABULARY BOT [1]"
    print "\a\a\a\a\a\a\a"

#====================================================================================================================================================#

def speech_to_text(audio):
    
    song = AudioSegment.from_mp3("audio.mp3")
    song.export("audio.wav", format="wav")  # Is the same as:
	
    time.sleep(2)
    with sr.AudioFile("audio.wav") as source:
        audio = r.record(source)
 
    try:
        text = r.recognize_google(audio)
        print("You said " + text)
        if(text == "tents"):
            text = "dense"
        if(text == "Tents"):
            text = "dense"
        if(text == "Bode"):
            text = "mode"
        if(text == "lute"):
            text = "loot"
        if(text == "heroin"):
            text = "harrowing"
        if(text == "and you were"):
            text = "inure"
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
 

def scrapper():
    try:
        alertObj = driver.switch_to.alert
        alertObj.accept()
        print "Alert detected!"
        driver.get(url)
    except Exception as e:
        print("No alert found!")
    driver.execute_script("""window.location.reload();""")
    time.sleep(2)
    global html
    global source
    global old_html
    global soup
    global op1
    global op2
    global op3
    global op4
    global options
    global word
    global lastAudioLen
    try:
	    html = driver.execute_script("return document.getElementsByTagName('body')[0].innerHTML;")
    except Exception as e:
        print("Error: " + str(e))
        time.sleep(1)
        driver.get(url)

    source = unidecode(html)

    old_html = source
    time.sleep(1)
    soup = BeautifulSoup(source, "html.parser")
    driver.execute_script("function getElementByXpath(path) { return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; }; window.getElementByXpath = getElementByXpath;")

    try:
        c = driver.find_element_by_class_name("wrapper").find_element_by_class_name("instructions").text
        if(c == "choose the best picture for"):
            driver.get(url)
            time.sleep(3)
            return 5
    except Exception as e:
        print "No img detected!"

    try:
        c = driver.find_element_by_class_name('next')
        if(c):
            nextQ = driver.find_element_by_class_name('next')
            nextQ.click()
            time.sleep(1)
            return 5
    except Exception as e:
        eee = str(e)
        print "No button detected! "

    try:
        isAudio = 0
        try:
            length_check = len(
            soup.findAll('div', attrs={'class': 'instructions'})[0].text.split(" "))
            if(length_check == 0):
                isAudio = 1
        except Exception as e:
            isAudio = 1
            print "AUDIO!"

        c_list = driver.execute_script('return document.getElementsByClassName("spellit")') #driver.find_elements_by_class_name('spellit')
        len_list = len(c_list) - 1
        if(isAudio):
            lastAudioLen = len_list - 1
        print "AUDIO: " + str(len_list)
        print str(c_list)
        c = c_list[len_list]
        if(c and lastAudioLen != len(c_list)):
            print "SPEACH DETECTED! LIST: " + str(len_list)
            if(skipAudio):
                time.sleep(1)
                text_area = driver.find_element_by_class_name('wordspelling')
                text_area.send_keys("Life is good (LG)")
                time.sleep(1)
                try:
                    c.click()
                    time.sleep(1)
                    c.click()
                    time.sleep(1)
                    c.click()
                    time.sleep(1)
                    element2 = driver.find_element_by_class_name('surrender')
                    element2.click()
                    time.sleep(2)
                    element3 = driver.find_element_by_class_name('next')
                    element3.click()
                    time.sleep(1)
                    element4 = driver.find_element_by_class_name('next')
                    element4.click()
                    driver.get(url)
                    time.sleep(3)
                except Exception as e:
                    a = str(e)
                    print "Error at: " + a
            else:
                try:
                    lastAudioLen = len(c_list)
                    audio = driver.find_element_by_class_name('playword')
                    #link_ = driver.execute_script("""return jQuery(".challenge-slide").data().audio;""")
                    link_ = driver.execute_script("""var list = document.getElementsByClassName("challenge-slide"); var obj = list[list.length - 1]; return jQuery(obj).data().audio;""")
                    link = ''.join(["https://audio.vocab.com/1.0/us/", link_, ".mp3"])
                    time.sleep(1)
                    print link

                    testfile = urllib.URLopener()
                    testfile.retrieve(link, "audio.mp3")

                    print "Downloading..."
                    time.sleep(2)
					
                    text = speech_to_text("audio.mp3")
                    time.sleep(1)
                    text_area_list = driver.find_elements_by_class_name('wordspelling')
                    text_area = text_area_list[len(text_area_list) - 1]
                    text_area.send_keys(text)
                    time.sleep(2)
                    c = c_list[len_list]
                    c.click()
                    time.sleep(2)
                    element4 = driver.find_element_by_class_name('next')
                    element4.click()
                    time.sleep(1)
                except Exception as e:
                    a = str(e)
                    print "Error at: " + a
                
            return 5
    except Exception as e:
        eee = str(e)
        print "No speach detected!"
	
    try:
        length_check = len(
            soup.findAll('div', attrs={'class': 'instructions'})[0].text.split(" "))
        if(length_check != 0):

            word = driver.find_element_by_xpath("//strong[1]").text
            if(str(word) == ""):
                word = driver.find_element_by_class_name("sentence").find_element_by_xpath("//strong[1]").text
            dic_exceptions = ['and', 'up', 'as', 'if', 'the', 'who', 'has', 'a', 'an', 'to', 'for', 'from', 'is', 'where', 'when', 'why',
                              'how', 'which', 'of', 'one', "one's", 'or', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

            #========================== Options ==========================#
            val1 = driver.execute_script("""return window.getElementByXpath("//a[@accesskey='1A']").text""")
            val2 = driver.execute_script("""return window.getElementByXpath("//a[@accesskey='2B']").text""")
            val3 = driver.execute_script("""return window.getElementByXpath("//a[@accesskey='3C']").text""")
            val4 = driver.execute_script("""return window.getElementByXpath("//a[@accesskey='4D']").text""")
            op1 = (val1 + "\n").rstrip('\n').split(" ")
            op2 = (val2 + "\n").rstrip('\n').split(" ")
            op3 = (val3 + "\n").rstrip('\n').split(" ")
            op4 = (val4 + "\n").rstrip('\n').split(" ")
            final = []
            options = [op1, op2, op3, op4]
            #========================== Options ==========================#
            op_st = ''.join(["Options: ", str(options)])
            #print op_st
            for option in options:
                for item in option:
                    for x in dic_exceptions:
                        if x == item:
                            p = option.index(x)
                            option.pop(p)

            #========================== Options Rading ==========================#
            s_link = "https://www.vocabulary.com/dictionary/"
            link = s_link + word
            html = urllib2.urlopen(link)
            soup = BeautifulSoup(html, "html.parser")
            if(word == "________"):
                return 0

            source_dic2 = None
            print "Word: " + word
            try:
                
                test = soup.find('div', {"class" : "definitionsContainer"})
                source_dic2 = unidecode(test.prettify())
                
            except Exception as e:
                eee = str(e)
                print "Error" + eee
                return 0

            
            
            a = 0

            rate_arr = []
            cpy_rate_arr = []
            for option in options:
                for item in option:
                    if item in source_dic2:
                        a += 1

                print ("{0} -> {1}".format(option, a))
                rate_arr.append(a)
                a = 0
            #========================== Options Rading ==========================#

            cpy_rate_arr = sorted(rate_arr)
            x_pos = cpy_rate_arr[len(cpy_rate_arr) - 1]
            x_pos_2 = cpy_rate_arr[len(cpy_rate_arr) - 2]
            choice = rate_arr.index(max(rate_arr))
            if (x_pos == x_pos_2):
                print "No position found."
            
            h = choice
            print h
            return h

        else:
            driver.quit
            print "Error: length_check is less or equal to 0"

    except Exception as e:
        print e

def click_op(i):
    try:
        if(i == 5):
            time.sleep(1)
            option_high_score = scrapper()
            time.sleep(1)
            click_op(option_high_score)
            return
        op = i + 1
        ar = ["", "A", "B", "C", "D"]
        high = str(op)
        b = ''.join([high, ar[op]])
        element = driver.find_element_by_xpath('//a[@accesskey="' + b + '"]')
        try:
            element.click()
        except Exception as e:
            a = str(e)
            print "Error at: " + a

        try:
            nextQ = driver.find_element_by_class_name('next')
            nextQ.click()
        except Exception as e:
            option_high_score = scrapper()
            time.sleep(1)
            click_op(option_high_score)
            a = str(e)
            print "Error quitting... " . a
    
        time.sleep(1)
        option_high_score = scrapper()
        time.sleep(1)
        click_op(option_high_score)
    except Exception as e:
        option_high_score = scrapper()
        time.sleep(1)
        click_op(option_high_score)
        a = str(e)
        print "Error quitting... " . a
#====================================================================================================================================================#
def autoUpdate(): #main()
    updated = update("https://raw.githubusercontent.com/lefela4/Vocabulary.com-AutoBot/master/src/vocab_Demo1.py", __version__)

    if(updated == 0):
        # Nothing to update
        main()
        
    elif(updated == 1):
        # The file have been updated!
        print("Please restart the program!")
    elif(updated == 2):
		# Error
        print("Sorry, an error occurred while preparing the installation. Please go in https://github.com/lefela4/Vocabulary.com-AutoBot/issues and create a new issue with the screen shot of the error!")
autoUpdate()

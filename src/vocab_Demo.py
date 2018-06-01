import os
import platform
from selenium import webdriver
import time
from unidecode import unidecode
import urllib2
#from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

_author_ = "Sayan Bhowmik"
fo = open('cred')
__version__ = "1.1"
############################################################################
# Link to  assignment [For Demo]
#url = "https://www.vocabulary.com/lists/23380/practice"
url = "https://www.vocabulary.com/lists/194479/practice"
#url = "https://www.vocabulary.com/lists/52473/practice"
##############################################################################


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "excludeSwitches", ["ignore-certificate-errors"])
check_driver_version = 1
driver = webdriver.Chrome(chrome_options=chrome_options)
#====================================================================================================================================================#
login_page = "https://www.vocabulary.com/login/"
a_page = url
my_username = fo.readlines()[0]
fo.seek(0, 0)
my_pass = fo.readlines()[1]
print annotate
print "[+] STARTING VOCABULARY BOT"
#key = str(raw_input("Enter Key Provided:"))
usr = ""
base = ""
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
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys(my_username)
    password.send_keys(my_pass)
    driver.find_element_by_class_name("green").click()


#====================================================================================================================================================#
def assignment():
    time.sleep(3)
    driver.get(a_page)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 280)")
    option_high_score = scrapper()
    click_op(option_high_score)
    print "[+] STARTING VOCABULARY BOT"
    print "\a\a\a\a\a\a\a"

#====================================================================================================================================================#


def scrapper():
    time.sleep(3)
    source = unidecode(driver.page_source)
    soup = BeautifulSoup(source, "html.parser")

    #htmlstring= soup.prettify()
    try:
    # print soup.findAll('div',
    # attrs={'class':'questionContent'})[0].text.split(" ")
        length_check = len(
            soup.findAll('div', attrs={'class': 'questionContent'})[0].text.split(" "))
        if(length_check == 1):
            # print "\n\n"
            time.sleep(3)
            word = soup.findAll('strong')[3].text
            # print"\n\n"

            dic_exceptions = ['up', 'as', 'if', 'the', 'who', 'has', 'a', 'an', 'to', 'for', 'from', 'is', 'where', 'when', 'why',
                              'how', 'which', 'of', 'one', "one's", 'or', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

                            #================================  Options ==========================#

            op1 = (soup.findAll('a', attrs={'accesskey': '1'})[
                   0].text + "\n").rstrip('\n').split(" ")
            op2 = (soup.findAll('a', attrs={'accesskey': '2'})[
                   0].text + "\n").rstrip('\n').split(" ")
            op3 = (soup.findAll('a', attrs={'accesskey': '3'})[
                   0].text + "\n").rstrip('\n').split(" ")
            op4 = (soup.findAll('a', attrs={'accesskey': '4'})[
                   0].text + "\n").rstrip('\n').split(" ")
            final = []
            options = [op1, op2, op3, op4]
                            #================================  Options ==========================#

            for option in options:
                for item in option:
                    for x in dic_exceptions:
                        if x == item:
                            p = option.index(x)
                            option.pop(p)

                    #================================  Option Rating ==========================#
            s_link = "https://www.vocabulary.com/dictionary/"
            link = s_link + word
            html = urllib2.urlopen(link)
            soup = BeautifulSoup(html, "html.parser")
            a = 0
            source_dic = unidecode(soup.prettify())
            rate_arr = []
            cpy_rate_arr = []

            for option in options:
                for item in option:
                    if item in source_dic:
                        a += 1

                print ("{0} -> {1}".format(option, a))
                rate_arr.append(a)
                a = 0
                    #================================  Option Rating ==========================#

            cpy_rate_arr = sorted(rate_arr)
            print "\n"
            print rate_arr
            print "\n"

            x_pos = cpy_rate_arr[len(cpy_rate_arr) - 1]
            x_pos_2 = cpy_rate_arr[len(cpy_rate_arr) - 2]

            if (x_pos == x_pos_2):
                driver.quit
                main()

            h = rate_arr.index(x_pos)

            return h

        else:
            driver.quit
            main()

    except IndexError:
        driver.quit
        main()


def click_op(i):

    op = i + 1
    high = str(op)
    element = driver.find_element_by_xpath('//a[@accesskey=' + high + ']')
    try:
        element.click()
    except:
        driver.quit
        main()

    time.sleep(3)

    nextQ = driver.find_element_by_class_name('nextQuestion')
    try:
        nextQ.click()
    except:
        driver.quit
        main()

    option_high_score = scrapper()
    time.sleep(1)
    click_op(option_high_score)


#====================================================================================================================================================#
main()

from flask import Flask, request, render_template
import json


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
#import requests
import re
import nltk
import json
from pyzipcode import Pyzipcode as pz
import unittest
import pyzipcode
from uszipcode import ZipcodeSearchEngine
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import sqlite3
import webbrowser  


import requests
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_welcome():
    return 'Hello, welcome to my new flask app. I made it! <br/> <br/> <i> Click <a href="http://localhost:5000/soundcloud">here</a> to continue on to my next route </i>'


@app.route('/soundcloud', methods= ['POST','GET'])
def scform():
    return render_template('custom_template1.html')



def parseSoundcloud(x):
  
    z = str(x)
    # chromedriver = "files/chromedriver"
    # os.environ["webdriver.chrome.driver"] = chromedriver
    # driver = webdriver.Chrome(chromedriver)
    ####Possibility of opening the window of each account that is searched through, rather than doing it through phantom
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    url = 'https://soundcloud.com/'+str(x)+'/tracks'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    songlinks=[]

    scheight = .1
    while scheight < 9.9:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight += .01
    #scrolls through the entire webpage so that all the songs are found, not just the first 10

    elem = driver.find_element_by_tag_name('a')

    for x in driver.find_elements_by_class_name('soundTitle__title'):
    #finds the link to each song of each user
        songlinks.append(x.get_attribute('href'))
    #stores this in a list
    driver.quit()

    #return 'Here are the links to each of the songs found on this account: <br> <br>' + str('<br>'.join(songlinks))

    return render_template('custom_template2.html', songlinks=songlinks)



@app.route('/yoursc')

        
        # params = {}
        # params['x'] = result.get('artist')
        # params['limit'] = result.get('num')
        # resp = requests.get('https://itunes.apple.com/search?', params = params)
        # data = json.loads(resp.text)
        #return x
		#return r
		#return render_template('custom_template2.html', objects = r)#, results = data['results'])



def yoursc():
    if request.method == 'GET':
        result = request.args
        x = result.get('sc')
        return parseSoundcloud(x)
    
# def soundcloud():
#   if request.method == 'GET':
#         result = request.args
#         x = result.get('account')
#         return parseSoundcloud(x)





if __name__ == '__main__':
    app.run(debug = True)


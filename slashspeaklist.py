#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess
import time,re

Url = "http://slashdot.org"

#html = urlopen(Url)
stories = list()

def say_title(title):
    try:
        if title:
            subprocess.call('echo '+title+'|/usr/bin/festival --tts',shell=True)
    except Exception as e:
        print(e)

while(True):
    if (datetime.now().hour >= 7 and datetime.now().hour <=20):
        html = urlopen(Url)
        bsObj=BeautifulSoup(html,"lxml")
        for story in bsObj.findAll("span",{"class":"story-title"}):
            try:
                if story not in stories:
                    stories.append(story)
                    title = story.find("a").text
                    print(title)
                    safe_title= re.sub(r'[^\w\s]','',title)
                    say_title(str(safe_title))
            except Exception as e:
                print(e)
    time.sleep(360)

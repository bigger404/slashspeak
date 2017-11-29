#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess

Url = "http://slashdot.org"

html = urlopen(Url)
#soup = BeautifulSoup(html)

#bsObj=BeautifulSoup(html)#.findAll("span",{"class":"story-title"})
bsObj=BeautifulSoup(html,"lxml")
for story in bsObj.findAll("span",{"class":"story-title"}):
	title = story.find("a").text
	print(title)
	try:
		if title:
			subprocess.call('echo '+title+'|/usr/bin/festival --tts',shell=True)
	except Exception as e:
		#print(e)
		print("bug")		

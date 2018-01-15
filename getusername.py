
from github import Github
import urllib2
from bs4 import BeautifulSoup
import re
import sys




f = open("allusers.txt")
for user in f.readlines():
	userlink = ("http://www.github.com/"+ user)
	website=urllib2.urlopen(userlink)
	soup = BeautifulSoup(website, "lxml")
	sys.stdout=open("test1.txt","a")
	print soup.title.string
	print userlink
sys.stdout.close()

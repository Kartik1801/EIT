#Search for meaning of a word and fetches it online.
from datetime import date
import requests
from bs4 import BeautifulSoup

def get_prononciation(word):
    word = (word.lower()).strip()
    URL= 'https://www.dictionary.com/browse/'+word
    page=requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    prononciation=soup.find(class_='pron-spell-content css-1ksa987 evh0tcl1')
    return prononciation.text
def get_wordtype(word):
    word = (word.lower()).strip()
    URL= 'https://www.dictionary.com/browse/'+word
    page=requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    wordtype=soup.find(class_='css-chpztc e1hk9ate2')
    return wordtype.text
def get_meaning(word):
    word = (word.lower()).strip()
    URL= 'https://www.dictionary.com/browse/'+word
    page=requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    meaning=soup.find(class_='one-click-content css-ibc84h e1q3nk1v1')
    return meaning.text
def get_WoD(): 
    URL= 'https://www.dictionary.com/e/word-of-the-day'
    page=requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    word=soup.find(class_='otd-item-headword__word')
    #defination=soup.find(class_='otd-item-headword__pos')
    w=word.text
    w=w.strip("\n")
    return w

#following piece of code extracts article from brief section of TOI(Times of India)
from newspaper import Article 
from bs4 import BeautifulSoup
import requests
import random
#to get link on news article from briefs section of toi and store all the brief article's link in list
def get_random_article():
    link=requests.get("https://timesofindia.indiatimes.com/briefs")
    soup=BeautifulSoup(link.content,'html.parser')
    res=soup.find(id='content')
    briefs = res.find_all('div', class_='brief_box')
    links = []
    for link in soup.find_all('div',attrs={"class":"brief_box"}):
        if(link.find('a')):
         links.append(link.find('a')['href'])
    l=random.choice(links)          
    #A new article from TOI 
    url = "https://timesofindia.indiatimes.com"+l
    #For different language newspaper refer above table 
    toi_article = Article(url, language="en") # en for English 
    #To download the article 
    toi_article.download() 
    #To parse the article 
    toi_article.parse() 
    #To perform natural language processing ie..nlp:: yet to study and implement 
    #toi_article.nlp()  
    #extracts text 
    return toi_article
def get_article_title(toi_article):
    #extracts title
    t=toi_article.title 
    return t    
def get_article_text(toi_article):
    t=toi_article.text 
    return t

# art=get_random_article() 
# text=get_article_text(art)
# title=get_article_title(art)
# print(type(art))   
# print(title.strip())
# print(text.strip())
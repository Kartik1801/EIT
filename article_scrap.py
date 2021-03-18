#following piece of code extracts article from brief section of TOI(Times of India)
from newspaper import Article 
from bs4 import BeautifulSoup
import requests

#to get link on news article from briefs section of toi and store all the brief article's link in list
link=requests.get("https://timesofindia.indiatimes.com/briefs")
soup=BeautifulSoup(link.content,'html.parser')
res=soup.find(id='content')
briefs = res.find_all('div', class_='brief_box')
links = []
for link in soup.find_all('div',attrs={"class":"brief_box"}):
    if(link.find('a')):
        links.append(link.find('a')['href'])
       
#A new article from TOI 
url = "https://timesofindia.indiatimes.com"+links[0]

#For different language newspaper refer above table 
toi_article = Article(url, language="en") # en for English 

#To download the article 
toi_article.download() 

#To parse the article 
toi_article.parse() 

#To perform natural language processing ie..nlp:: yet to study and implement 
#toi_article.nlp() 

#extracts title 
print("Article's Title:") 
print(toi_article.title) 
#print("\n") 

#extracts text 
print("Article's Text:") 
print(toi_article.text) 
#print("\n") 

#extracts summary 
#print("Article's Summary:") 
#print(toi_article.summary) 
#print("\n") 

#extracts keywords 
#print("Article's Keywords:") 
#print(toi_article.keywords) 
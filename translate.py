from googletrans import Translator
from article_scrap import get_article_text,get_article_title,get_random_article,t2s

def translate_text(sentence,lang):
    translator= Translator()
    return(translator.translate(sentence, dest=lang).text)

# art=get_random_article() 
# text=get_article_text(art)
# title=get_article_title(art)
# # print(title)
# print(translate_hindi(title.strip(),'hi'))
# print(translate_hindi(text.strip(),'hi'))
# t2s(title.strip())

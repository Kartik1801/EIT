from gtts import gTTS
import os
import playsound
def t2s(word):

        pronunciation=gTTS(text=word, lang='en',slow=False)
        pronunciation.save("a.mp3")
        p =os.path.abspath("a.mp3")
        playsound.playsound(p,True)  
        os.remove("a.mp3")             
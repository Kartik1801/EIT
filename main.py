from mainui import Ui_MainWindow
from more_ui import Ui_menu_window
from translate import translate_text
from dictui import Ui_Dict_Window
from history import getdailywordhistory
from readarticleui import  Ui_read_window
from chatbotui import Ui_MainWindow as Ui_Chat
from chatbot import bot,trainbot
from TranslateUI import Ui_TranslateWindow
from PyQt5 import QtWidgets, uic
from article_scrap import get_article_text,get_article_title,get_random_article
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtMultimedia
from fetch_def import get_meaning, get_wordtype, get_prononciation, get_WoD
from tts import t2s as texttospeech
import sys
import random
flag =0

class ChatWindow(QtWidgets.QMainWindow ,Ui_Chat):
    def  __init__(self,*args,obj=None,**kwaargs):
        super(ChatWindow,self).__init__(*args,**kwaargs)
        self.setupUi(self)
        self.show()
        try:
            trainbot(bot)
        except:
            Print("bot trained already")
        self.send_button.clicked.connect(self.sendmessage)
        self.textEdit.setText(" Hello I am a bot, I love to talk to people, let's chat")
        
    def sendmessage(self):
        try:
            user_input=self.chat_input.text()
            self.textEdit.append("You:"+str(user_input))
            bot_response = bot.get_response(user_input)
            self.textEdit.append("Bot:"+str(bot_response))
            self.chat_input.clear()
        except:
            self.textEdit.append("Bot:"+"Sorry I couldnt understand!")

class Translate_Window(QtWidgets.QMainWindow,Ui_TranslateWindow):
    def __init__(self,*args,obj=None,**kwaargs):
        super(Translate_Window,self).__init__(*args,**kwaargs)
        self.setupUi(self)
        self.show()
        self.ttHindi.clicked.connect(self.translatetoHindi)
        self.ttEnglish.clicked.connect(self.translatetoEnglish)
    def translatetoHindi(self):
        user_input=self.InputText.toPlainText()
        self.TranslatedText.setText(translate_text(user_input,"hi"))
    def translatetoEnglish(self):
        user_input=self.InputText.toPlainText()
        self.TranslatedText.setText(translate_text(user_input,"en"))
        
class Read_article_window(QtWidgets.QMainWindow,Ui_read_window):
    def  __init__(self,*args,obj=None,**kwaargs):
        super(Read_article_window,self).__init__(*args,**kwaargs)
        self.setupUi(self)
        self.set_Values()
        self.refresh_button.clicked.connect(lambda:self.set_Values())
        self.t2s_button.clicked.connect(lambda:self.gtts())
        self.more_button.clicked.connect(self.show_menu)
        self.homw_button.clicked.connect(self.show_main)
        self.exit_button.clicked.connect(lambda:self.close())
    def show_menu(self):
        self.w=menu_window()
        self.w.show()    
    def set_Values(self):
        _translate = QtCore.QCoreApplication.translate
        article=get_random_article()
        article_title=get_article_title(article)
        article_text=get_article_text(article)
        self.article_title.setText(_translate("Read_article_window", article_title))
        self.article_text.setText(_translate("Read_article_window", article_text))
        self.show()
    def show_main(self):
        self.w=Main_Window()
        self.w.show()
        self.hide()
    def gtts(self):
        t=self.article_text.toPlainText()
        texttospeech(t)
        
       
class Dict_Window(QtWidgets.QMainWindow,Ui_Dict_Window):
    def __init__(self,*args,obj=None,**kwargs):
        super(Dict_Window,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.search_button.clicked.connect(lambda:self.set_Values())
        self.t2s_button.clicked.connect(lambda:self.gtts())
        self.home_button.clicked.connect(self.show_main)
        self.more_button.clicked.connect(self.show_menu)
        self.exit_button.clicked.connect(lambda:self.close())
    def getInput(self):
        _translate = QtCore.QCoreApplication.translate
        input=self.search_input.toPlainText()
        if(input!=""):
         return input.strip()
        else:
         self.word.setText(_translate("Dict_Window", "No word Entered"))
    def set_Values(self):
        _translate = QtCore.QCoreApplication.translate
        word=self.getInput()
        self.word.setText(_translate("Dict_Window", word))
        self.word_def.setText(_translate("Dict_Window", get_meaning(word)))
        self.pronunciation.setText(_translate("Dict_Window", get_prononciation(word)))
        self.word_type.setText(_translate("Dict_Window", get_wordtype(word)))
    def show_menu(self):
        self.w=menu_window()
        self.w.show()    
    def show_main(self):
        self.w=Main_Window()
        self.w.show()
        self.hide()
    def gtts(self):
        w=self.getInput()
        texttospeech(w)
                
class menu_window(QtWidgets.QMainWindow,Ui_menu_window):
    def __init__(self,*args,obj=None,**kwargs):
        super(menu_window,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.Article_button.clicked.connect(self.show_article)
        self.translator_button.clicked.connect(self.show_translate)
        self.Chat_button.clicked.connect(self.show_chatbot)
        self.Exit_button.clicked.connect(lambda:self.close())
        self.show()
    def show_article(self):
        self.w=Read_article_window()
        self.w.show()
        self.hide()

    def show_translate(self):
        self.w=Translate_Window()
        self.w.show()
        self.hide()
    def show_chatbot(self):
        self.w=ChatWindow()
        self.w.show()
        self.hide()

class Main_Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,obj=None,**kwargs):
        super(Main_Window,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.set_Values()
        self.dictionary_button.clicked.connect(self.show_dict)
        self.more_button.clicked.connect(self.show_menu)
        self.t2s_button.clicked.connect(lambda:self.gtts())
    def show_menu(self):
        self.w=menu_window()
        self.w.show()    
    def set_Values(self):
        _translate = QtCore.QCoreApplication.translate
        w=get_WoD()
        self.wod_word.setText(_translate("Main_Window", w))
        self.wod_def.setText(_translate("Main_Window", get_meaning(w)))
        self.wod_pronunciation.setText(_translate("Main_Window", get_prononciation(w)))
        self.wod_type.setText(_translate("Main_Window", get_wordtype(w)))
        self.exit_button.clicked.connect(lambda:self.close())
        d=getdailywordhistory()
        for v in d:
            self.createLabel(v)
        self.show()
    def show_dict(self):
        self.w=Dict_Window()
        self.w.show()
        self.hide()
    def gtts(self):
        w=get_WoD()
        texttospeech(w)
           
    def createLabel(self,d):
        _translate=QtCore.QCoreApplication.translate
        sa_label7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sa_label7.setMinimumSize(QtCore.QSize(0, 40))
        sa_label7.setStyleSheet("font: 12pt \"Cambria\";\n"
"border-bottom:1px solid rgb(0,0,0);")
        sa_label7.setText("")
        sa_label7.setScaledContents(True)
        sa_label7.setObjectName("sa_label7")
        self.verticalLayout.addWidget(sa_label7, 0, QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        sa_label7.setText(_translate("Main_Window", d))

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window= Main_Window()
    sys.exit(app.exec_())

from dictui import Ui_Dict_Window
from mainui import Ui_MainWindow
from history import getdailywordhistory
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets
from fetch_def import get_meaning, get_wordtype, get_prononciation, get_WoD
from tts import t2s as texttospeech
import sys
import random


class Dict_Window(QtWidgets.QMainWindow,Ui_Dict_Window):
    def __init__(self,*args,obj=None,**kwargs):
        super(Dict_Window,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.search_button.clicked.connect(lambda:self.set_Values())
        self.t2s_button.clicked.connect(lambda:self.gtts())
        self.home_button.clicked.connect(self.show_main)
#        self.more_button.clicked.connect(self.show_anagram)
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
    # def show_anagram(self):
    #         self.w=Anagram_Window()
    #         self.w.show()
    #         self.hide()    
    def show_main(self):
        self.w=Main_Window()
        self.w.show()
        self.hide()
    def gtts(self):
        w=self.getInput()
        texttospeech(w)

# class Anagram_Window(QtWidgets.QMainWindow,Ui_Anagram):
#     def __init__(self,*args,obj=None,**kwargs):
#         super(Anagram_Window,self).__init__(*args,**kwargs)
#         self.setupUi(self)
#         self.set_Values()
#         self.exit_button.clicked.connect(lambda:self.close())
#         self.Next_Button.clicked.connect(lambda:self.getValue())
#     def set_Values(self):
#         p=choose()
#         j=jumble(p)
#         _translate = QtCore.QCoreApplication.translate
#         self.jword.setText(_translate("Anagram_Window",j))
#         self.submit_button.clicked.connect(lambda:self.checkans(p))
#     def getValue(self):
#         p=choose()
#         _translate = QtCore.QCoreApplication.translate
#         j=jumble(p)
#         self.jword.setText(_translate("Anagram_Window",j))
#         self.submit_button.clicked.connect(lambda:self.checkans(p))
#     def checkans(self,p):
#         _translate = QtCore.QCoreApplication.translate
#         ans=self.input.toPlainText()
#         if (p==ans):
#             self.label_3.setText(_translate("Anagram_Window","CORRECT!!"))
#         else:
#             self.label_3.setText(_translate("Anagram_Window","INCORRECT!!"))
        
class Main_Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,obj=None,**kwargs):
        super(Main_Window,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.set_Values()
        self.dictionary_button.clicked.connect(self.show_dict)
#        self.more_button.clicked.connect(self.show_anagram)
        self.t2s_button.clicked.connect(lambda:self.gtts())
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
    sys.exit(app.exec())

from chatbotui import Ui_MainWindow
from chatbot import bot,trainbot
from PyQt5 import QtCore, QtGui, QtWidgets ,uic
import sys


class ChatWindow(QtWidgets.QMainWindow ,Ui_MainWindow):
    def  __init__(self,*args,obj=None,**kwaargs):
        super(ChatWindow,self).__init__(*args,**kwaargs)
        self.setupUi(self)
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

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window= ChatWindow()
    window.show()
    sys.exit(app.exec())




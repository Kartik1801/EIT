#Extracts a new word daily from dictionary.com
# to install win toast : pip install win10toast-click
from win10toast_click import ToastNotifier #will be used to pop notification
from dictui import Ui_Dict_Window
from mainui import Ui_MainWindow
from history import getdailywordhistory
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets
from fetch_def import get_meaning, get_wordtype, get_prononciation, get_WoD
from tts import t2s
import sys
import random

from fetch_def import get_meaning
from daily_fetch import dailyword
from main import Main_Window
def fun():
    app=QtWidgets.QApplication(sys.argv)
    Main_Window()
    sys.exit(app.exec_())

w=get_WoD()
WoD=w   + '''
meaning:  '''+ get_meaning(w)
toaster=ToastNotifier()
toaster.show_toast("Word of the day",WoD, icon_path=None, duration=10, callback_on_click=lambda: fun())
dailyword(w)
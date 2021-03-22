import sqlite3
from datetime import date
from fetch_def import get_meaning
from fetch_def import get_wordtype
from fetch_def import get_prononciation
from fetch_def import get_WoD

def dailyword(w):
    today=str(date.today())
    conn=sqlite3.connect('word.db')
    cn= conn.cursor()
    try:
                x= "INSERT INTO dailywords VALUES ('"+ w +  "','" +get_meaning(w)+"','" +get_prononciation(w) + "','" + get_wordtype(w) + "','" + today +"')"
                cn.execute(x)
                conn.commit()
    except: 
                print("value added in database")

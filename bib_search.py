	# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:06:05 2020
Laboraufgabe Suche-Programm für Bibiliotheksdatenbank
@author: Lennard Schröder und Tjark  Ziehm
"""





#########################IMPORT#########################
import numpy as np
import pandas as pd
import sys
if "tkinter" not in sys.modules:
    from tkinter import *
#from PIL import ImageTk, Image   
from functools import partial

import os
import csv



from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

#########################Grundeinstellungen#########################
'''Setzen vom Workingdirectory'''
print(os.getcwd())
os.chdir('C:\\Users\\color\\OneDrive\\Dokumente\\AUD\\LABOR')
print(os.getcwd())

#Anfrage_ISBN = int(input())

#########################GUI#########################

def von_begruessungsfenster_zu_suchfenster():
    Fenster2.mainloop()
    return

def wechsel_schrift1():
    Begruessungstext1["bg"]="#000000"
    Begruessungstext1["fg"]="#FFFFFF"
    Begruessungstext1["font"]="Arial 10 italic"
    Begruessungstext1["height"]=2
    Begruessungstext1["width"]=20
    Begruessungstext11["anchor"]="w"     
    return

def wechsel_schrift2(): 
    Begruessungstext1["bg"]="#FF0000"
    Begruessungstext1["fg"]="#FFFFFF"
    Begruessungstext1["font"]="Arial 10 bold"
    Begruessungstext1["height"]=2
    Begruessungstext1["width"]=20      
    return
    
def change_label_number(num):
    counter = int(str(labelExample['text']))    
    counter += num
    labelExample.config(text=str(counter))
    
def gebe_isbn():
    isbn_label["text"]=sucheingabe.get()
    isbn_eingabe = int(isbn_label["text"])
    print("isbn eingegeben:", str(isbn_eingabe))
    return isbn_eingabe

def isbn_spalte_durchsuchen(isbn_eingabe):
    isbn_eingabe=isbn_eingabe
    for value in df_pd["book_isbn"]:
        if value == isbn_eingabe:
            print("Buch gefunden")
        
#########################GUI-Variablen#########################


#-------------------------Suchseite 
app_side2 = tk.Tk()
app_side2.title("Suchseite")
app_side2.geometry("1100x700")

#-------------------------Label
Suchtext2= tk.Label(app_side2, text="Bitte gebe die gesuchte ISBN Nummer ein. Diese ist 10 oder 13 Zahlen lang.",width=100)
isbn_eingegeben = tk.Label(app_side2, text= "Du  hast folgende ISBN eingegeben:")
isbn_label = tk.Label(app_side2)

#-------------------------Button
such_button= tk.Button(app_side2,text ="Suche starten",command=gebe_isbn)
abbruch_button = tk.Button(app_side2,text="Suche abbrechen")

#-------------------------Frame
app_s2_frame = tk.Frame(app_side2)

#-------------------------Entry
sucheingabe = tk.Entry(app_side2, width = 30)

#-------------------------Widgets platzieren
sucheingabe.grid(row=1, column=0)


#-------------------------Einbinden
sucheingabe.pack()
Suchtext2.pack()
such_button.pack()
abbruch_button.pack()
isbn_eingegeben.pack()
isbn_label.pack()

##########################Begrüßungsseite##########################
#-------------------------Begrüßungsseite
app = tk.Tk()
app.title("Willkommen bei der Suchmaschine der  FH Kiel!")
app.geometry("1100x700")


#-------------------------Label             
#lab1 = tk.Label(app,text = "test1") 
##lab2 = tk.Label(app,text = "test2")
#lab3 = tk.Label(app,text = "test3")
#lab4 = tk.Label(app,text = "test4")
Begruessungstext1= tk.Label(app, text="Möchtest du gleich suchen ?",width=50)

#-------------------------Button
buttonExample = tk.Button(app, text="Suche starten", width=20,command=partial(change_label_number, 1))
buttonExample2 = tk.Button(app, text="Suche beenden", width=20,command=partial(change_label_number, 2))
buttonExample3 = tk.Button(app, text="Anderungen", width=20)
#labelExample = tk.Button(app, text="0")

#-------------------------Frame
#frame1.grid(row=1,column=0)

#-------------------------Widgets platzieren

#lab1.grid(text="zurück",row=0,column=1)
#lab2.grid(text="abbrechen",row=0,column=2)
#lab3.grid(text="start"row=0,column=3)
#lab4.grid(row=0,column=4)


#img1 = tk.PhotoImage(file='C:\\Users\\color\\OneDrive\\Dokumente\\AUD\\LABOR\\fh2.gif'
#img_label = tk.Label(app,image=img1)




#img_label.pack()
Begruessungstext1.pack()    
buttonExample.pack()
buttonExample2.pack()
buttonExample3.pack()   



#########################Variablen#########################
file = 'buch_1.csv' 


	
#########################Funktionen#########################
def main():
    print("Programm gestartet")
    app_side2.mainloop()
    
def erstelle_pd_datenbank(csv_df):
    csv_df = csv_df
    df_pd=pd.read_csv(csv_df,sep=',')
    return(df_pd)

# def erstelle_np_datenbank(csv_df):
#     csv_df = csv_df
#     df_np=np.genfromtxt(csv_df, dtype=None , delimiter = ',',names = True)
#     print(df_np)
    
def csv_oeffnen(file):
    file = file
    with open(file,'r',encoding = 'utf8')as csv_df:          
        erstelle_pd_datenbank(csv_df)
        #erstelle_np_datenbank(csv_df)
   

    
    


#########################MAIN#########################
main()
#csv_oeffnen(file)




#########################ANBINDUNGEN#########################


    



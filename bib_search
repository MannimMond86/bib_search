# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:06:05 2020
Laboraufgabe Suche-Programm für Bibiliotheksdatenbank
@author: Lennard Schröder und Tjark  Ziehm
"""





#########################IMPORT#########################
import numpy as np
import pandas as pd
import tkinter as tk
import os
import csv

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
    
Fenster1 = tk.Tk()

Fensterbezeichnung1 = tk.Label(Fenster1,text="Herzlich Willkommen bei deiner Suchmaschine in der Bibliothek").pack()
#Fensterbezeichnung1["bg"]="#FFFF00"
Begruessungstext = tk.Label(Fenster1,text="Hallo, hier kannst du schauen, ob dein gesuchtest Buch auf der Liste der Bibliothe ist. Möchtest du gleich suchen ?").pack()

Button_yes = tk.Button(Fenster1, text = "Ja", command = von_begruessungsfenster_zu_suchfenster).pack()
Button_no = tk.Button(Fenster1, text = "Nein").pack()

Fenster2 = tk.Tk()
    
#########################Variablen#########################
file = 'buch_1.csv' 


	
#########################Funktionen#########################
def main():
    Fenster1.mainloop()
    print("Programm gestartet")
    
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
csv_oeffnen(file)




#########################ANBINDUNGEN#########################


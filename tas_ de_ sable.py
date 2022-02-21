#######################################################
# GROUPE: 
# Sofiya RUGA
# Nathan  Villiers 
# Arthur Ponchelet 
# Cédric lesbast 
# https://github.com/uvsq-info/l1-python
#######################################################

#IMPORT DES LIBRAIRIES
import tkinter as tk
import random as r
from turtle import width



#DEFINITION DES CONSTANTES
m = int(input("coté de la grille"))

largeur=500
hauteur=500


#DEFINITION DES VARIABLES GLOBALES






#DEFINITION DES FONCTIONS
def test():
    print("le bouton marche")

#PROGRAMME

#---création de l'interface graphique
root = tk.Tk()

root.title("Tas De Sable")
root.geometry("1920x1080")
canvas = tk.Canvas(root,width=largeur,height=hauteur,bg="#000000")
canvas.grid(row=3,column=3,rowspan=1,columnspan=1)

bouton_config_alea = tk.Button(root, text="Clique pour Configuration Aléatoire",command=test)
bouton_config_alea.grid(row=0,column=0)

#---création de la grille
for i in range (m):
    canvas.create_line(((largeur/m)*i,0), ((largeur/m)*i, 500), fill="blue", width=2)
    canvas.create_line((0,(hauteur/m)*i), (500,(hauteur/m)*i), fill="blue", width=2)

L = [[0] * m] * m
print(L)

root.mainloop()
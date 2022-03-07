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
taillecarré=500/m
x0=1
y0=1
L=[]
configcourante=L  

#DEFINITION DES VARIABLES GLOBALES






#DEFINITION DES FONCTIONS
def test():
    print("le bouton marche")

def basique ():
    L=[]
    for i in range (m):
        L.append([])

        for k in range (m):

            try:
                L[i].append(0)

            except IndexError:
                continue
    print(L)

def aléatoire ():
    L=[]
    for i in range (m):
            L.append([])

            for k in range (m):

                try:

                    L[i].append(r.randint(0,4))
                

                except IndexError:
                    continue
    print(L)

def couleurs ():
    

#PROGRAMME

#---création de l'interface graphique
root = tk.Tk()

root.title("Tas De Sable")
root.geometry("1920x1080")
canvas = tk.Canvas(root,width=largeur,height=hauteur,bg="#000000")
canvas.grid(row=3,column=3,rowspan=1,columnspan=1)

bouton_config_alea = tk.Button(root, text="Clique pour Configuration Aléatoire",command=aléatoire)
bouton_config_alea.grid(row=0,column=0)
bouton_config_basique = tk.Button(root, text="Clique pour Configuration basique",command=basique)
bouton_config_basique.grid(row=1,column=0)
bouton_lancement = tk.Button(root, text="Clique pour colorer les cases",command=couleurs) 
bouton_lancement.grid(row=2,column=0)

#---création de la grille
for i in range (m):
    canvas.create_line(((largeur/m)*i,0), ((largeur/m)*i, 500), fill="#474747", width=1)
    canvas.create_line((0,(hauteur/m)*i), (500,(hauteur/m)*i), fill="#474747", width=1)

L = []



    
print(L)

root.mainloop()


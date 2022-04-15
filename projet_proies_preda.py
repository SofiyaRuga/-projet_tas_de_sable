#######################################################
# GROUPE: 
# Sofiya RUGA
# Nathan  Villiers 
# Arthur Ponchelet 
# Cédric lesbast 
#https://github.com/SofiyaRuga/-projet_tas_de_sable
#######################################################




import tkinter as tk
import random as r
from tracemalloc import stop
root = tk.Tk()
root.title("Tas De Sable")
root.geometry("1920x1080")




#


#demande le nombre de case et le nombre de proies souhaitées
nbrecase=int(input("nombre de cases de coté (conseillé 30)"))
nombreproie=int(input("nombre de proie"))
naissanceproie=int(input("entrez le nombre de naissance de proies par itération"))
vieproie=int(input("entrez la durée de vie (en itérations) des proies"))

cote=750  #int(input("taille du canvas(conseillé <750)"))
taillecase=float(cote/nbrecase)
x0=0
y0=0
canvas = tk.Canvas(root,width=cote,height=cote,bg="#000000")
canvas.grid(row=0,column=2,rowspan=4,columnspan=4)




#message d'erreur si l'utilisateur choisi trop de proies pour la capacité du terrain
if nombreproie>(nbrecase*nbrecase):
    print("Il ne peut pas y avoir autant de proies sur le terrain ! Relancez le script svp")
    exit()
    



#crée la grille et donc le nombre de cases totales
for i in range (nbrecase):
        canvas.create_line(((cote/nbrecase)*i,0), ((cote/nbrecase)*i, cote), fill="#474747", width=1)
        canvas.create_line((0,(cote/nbrecase)*i), (1080,(cote/nbrecase)*i), fill="#474747", width=1)

def tracagegrille():
    for i in range (nbrecase):
        canvas.create_line(((cote/nbrecase)*i,0), ((cote/nbrecase)*i, cote), fill="#474747", width=1)
        canvas.create_line((0,(cote/nbrecase)*i), (1080,(cote/nbrecase)*i), fill="#474747", width=1)
    




#crée une configuration vierge
def creationconfiguration ():
    global L
    L=[]
    for i in range (nbrecase):
        L.append([])
        for k in range (nbrecase):
            try:
                L[i].append(0)
            except IndexError :         #Ici, Nel m'a aidé :)
                continue
    global configuration 
    configuration = L
    print(L)



#place aléatoirement le nombre de proies choisies sur la config vierge existante, à des places uniques 
def creationconfigaleatoire ():
    global configaleatoire
    possible=[0]
    positions=0
    compteur=0
    while compteur!=nombreproie:
        positiony=int(r.randint(0,nbrecase-1))
        positionx=int(r.randint(0,nbrecase-1))
        positions=positiony,positionx
        if positions not in possible:
            possible.append(positions)
            L[positiony][positionx]=1
            compteur+=1
        
    configuration=L
    configaleatoire=configuration


        
#fonction qui, à chaque itération, rajoute le nombre de proies qui naissent dans la liste représentative
def naissance():               
    global nombreproie
    compte=0
    while compte!=naissanceproie:
        positionsy=int(r.randint(0,nbrecase-1))
        positionsx=int(r.randint(0,nbrecase-1))
        if L[positionsy][positionsx]==0:
            L[positionsy][positionsx]=1
            compte+=1
    nombreproie+=naissanceproie

        
            





#fonction qui détermine une itération, en déplacant chaque proie (déplacement des 1 dans la liste) et qui au passage 
#actualise leur nombre (en ajoutant les naissance -avec la fonction naissance-) 
def deplacement():
    global vieproie
    if nombreproie==nbrecase*nbrecase:                        #si le nombre de proie après l'ajout des naissance rempli complètement la grille, le script s'arrête
        print("les proies ont envahi le terrain !")
        exit()


    L_c = []
    for x in range(len(L)): 
        truc = [] 
        for elem in L[x]:         #ici, la fonction "copy()" ne fonctionnait pas, alors j'ai récup un script sur internet
            truc.append(elem)     #pour copier manuellement la liste L en une copie indépendante qui est scannée et qui n'est donc
        L_c.append(truc)          #pas modifiée pour pas troubler le scan


    for i in range(len(L_c)):
        for j in range (len(L_c[i])):
            if L_c[i][j]>=1 and L_c[i][j]<vieproie :
                hasard=r.randint(1,8)
                L[i][j]+=1
                if hasard==1 :     #monte en haut
                    if i>0:
                        if L[i-1][j]==0:
                            L[i-1][j],L[i][j]=L[i][j],L[i-1][j]
                            
                                 
                elif hasard==2:    #haut droite
                    if i>0 and j<nbrecase-1:
                        if L[i-1][j+1]==0:
                            L[i][j],L[i-1][j+1]=L[i-1][j+1],L[i][j]
                        
                elif hasard==3:     #droite  
                    if j<nbrecase-1:
                        if L[i][j+1]==0:
                            L[i][j],L[i][j+1]=L[i][j+1],L[i][j]
                        
                elif hasard==4:             #bas droite
                    if i<nbrecase-1 and j<nbrecase-1:
                        if L[i+1][j+1]==0:
                            L[i][j],L[i+1][j+1]=L[i+1][j+1],L[i][j]
                            
                elif hasard==5 :               #bas
                    if i<nbrecase-1:
                        if L[i+1][j]==0:
                            L[i][j],L[i+1][j]=L[i+1][j],L[i][j]
                            
                elif hasard==6 :          #bas gauche
                    if i<nbrecase-1 and j>0:
                        if L[i+1][j-1]==0:
                            L[i][j],L[i+1][j-1]=L[i+1][j-1],L[i][j]
                            
                elif hasard==7:            #gauche
                    if j>0:
                        if L[i][j-1]==0:
                            L[i][j],L[i][j-1]=L[i][j-1],L[i][j]
                            
                elif hasard==8:              #haut gauche
                    if i>0 and j>0:
                        if L[i-1][j-1]==0:
                            L[i][j],L[i-1][j-1]=L[i-1][j-1],L[i][j]      
            elif L_c[i][j]==vieproie:
                L[i][j]=0
    naissance()                         #ajoute les proies qui sont nées dans la liste représentative
    affichageproie()                    #actualise l'affichage des proies pour cette itération
    
    

 
  
                











        


#actualise l'affichage des proies sur le terrain en scannant les 1 et en traçant des carrés
def affichageproie():
    for i in range (len(L)):
        for j in range (len(L[i])):
            if L[i][j]>=1 and L[i][j]<4:
                canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill="white")
            elif L[i][j]==0:
                canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0+taillecase*(j+1),y0+taillecase*(i+1),fill="black")
            elif L[i][j]>=4 and L[i][j]<7:
                canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill="yellow")
            elif L[i][j]>=7:
                canvas.create_rectangle(x0 +taillecase*j,y0+taillecase*i,x0 +taillecase*(j+1),y0+taillecase*(i+1),fill="orange")
            
    tracagegrille()           #retrace la grille (du coup à chaque itération) car il y avait un pb d'affichage






#boutons
bouton_config_vide = tk.Button(root, text="créer une configuration vide",command=creationconfiguration)
bouton_config_vide.grid(row=0,column=0)

bouton_config_alea = tk.Button(root, text="mettre des proies aléatoirement",command=creationconfigaleatoire)
bouton_config_alea.grid(row=1,column=0)

bouton_affichage = tk.Button(root, text="afficher des proies",command=affichageproie)
bouton_affichage.grid(row=2,column=0)

bouton_deplace = tk.Button(root, text="faire se déplacer les proies",command=deplacement)
bouton_deplace.grid(row=3,column=0)


root.mainloop()
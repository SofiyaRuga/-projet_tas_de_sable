# -projet_proies_prédateur
#########################################
# groupe 
# SOFIYA RUGA 
# VILLIERS NATHAN 
# ARTHUR PONCHELET
# Cédric LESBATS 
# https://github.com/uvsq-info/l1-python


#########################################

Dans l'objectif de réaliser  le projet proies-prédateurs ,nous avons établies les lignes de codes suivantes,  
sauf l' étape 2 : La réproduction des proies , le programme ne permet pas  de sauvgarder la simulation dans un fichier et de la recharger, 
 pour finir aucune stratégie de fuite n'as été programmé pour les proies , malgrés une idée de mise en place.
 ###########################################################################################################################################
- importation des modules nécessaire au programme 
lignes 9 - 11

- création des constantes 
lignes 15 - 24
 
 -Création des classes Prey (proie) et Predator (prédateurs) dans lesquelles on implémente les caractéristiques d'âge (en itérations ) et d'énergie pour les Prey .
 lignes 27 - 36
   
   -Création des variables et de la fonction qui permettra de demander à l'utilisateur les paramètres qu'il souhaite utiliser pour sa simulation , il est possible de simplement valider chaque paramètre sans rien y inscrire , des valeurs "par défaut " ont été prévues. 
lignes 44 - 86
 
- Mise en place de la fenêtre graphique du projet .
lignes 88 - 98
  
-génération des proies et prédateurs sur des espaces vides.
lignes 100 - 116
  
  -Déplacement des individus et création du Flair des prédateurs ainsi que de leurs déplacements en fonction
 lignes 126 - 209 , 233 - 251 
 
-Création des fonctions qui serviront à la reproduction des espèces.
lignes 211 - 231
  
  -Fonctions permettant le changement de couleur des cases en présence des différents individus , on considère être dans une prairie , la couleur verte est donc celle du sol.
  lignes 259 - 284
    
-On termine par créer les boutons sur l'interface et on les rends actifs . 
lignes 292 - 373

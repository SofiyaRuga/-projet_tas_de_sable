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

import random as r
import tkinter as tk
import numpy as np 

- création des constantes 
MAP_SIZE = 30
N_PRO = 20
F_PRO = 2
A_PRO = 10
N_PRE = 10
A_PRE = 20
E_PRE = 10
MIAM = 5
FLAIR = 3
 
 
 -Création des classes Prey (proie) et Predator (prédateurs) dans lesquelles on implémente les caractéristiques d'âge (en itérations ) et d'énergie pour les Prey .
 
 class Prey:
  "Simulation prey class"
  def init(self, A_pro):
    self.age = A_pro
class Predator:
  "Simulation predator class"
  def init(self, A_pre, E_pre):
    self.age = A_pre
    self.energy = E_pre
   
   -Création des variables et de la fonction qui permettra de demander à l'utilisateur les paramètres qu'il souhaite utiliser pour sa simulation , il est possible de simplement valider chaque paramètre sans rien y inscrire , des valeurs "par défaut " ont été prévues. 

    def project_init():
  size = MAP_SIZE
  N_pro = N_PRO
  F_pro = F_PRO
  A_pro = A_PRO
  N_pre = N_PRE
  A_pre = A_PRE
  E_pre = E_PRE
  E_repro = E_REPRO
  
   size_input = input(f"Largeur  et hauteur du plateau ({MAP_SIZE} par défaut): ")
  if size_input != "":
    size = int(size_input)
  prey_input = input(f"Nombre de proies initial ({N_PRO} par défaut): ")
  if prey_input != "":
    N_pro = int(prey_input)
  f_prey_input = input(f"Fréquence de naissance des proies ({F_PRO} par défaut): ")
  if f_prey_input != "":
    F_pro = int(f_prey_input)
  a_prey_input = input(f"Durée de vie des proies ({A_PRO} par défaut): ")
  if a_prey_input != "":
    A_pro = int(a_prey_input)
  preda_input = input(f"Nombre de prédateurs initial ({N_PRE} par défaut): ")
  if preda_input != "":
    N_pre = int(preda_input)
  a_preda_input = input(f"Durée de vie des prédateurs ({A_PRE} par défaut): ")
  if a_preda_input != "":
    A_pre = int(a_preda_input)
  e_preda_input = input(f"Énergie des prédateurs ({E_PRE} par défaut): ")
  if e_preda_input != "":
    E_pre = int(e_preda_input)
  e_repro_preda_input = input(f"Énergie de reproduction des prédateurs ({E_REPRO} par défaut): ")
  if e_repro_preda_input != "":
    E_repro = int(e_repro_predainput)

  map = []
  for  in range(size):
    line = []
    for _ in range(size):
      line.append(0)
    map.append(line)

  return map, size, N_pro, F_pro, A_pro, N_pre, A_pre, E_pre, E_repro
    
- Mise en place de la fenêtre graphique du projet .

def window_init(size, map):
  window = tk.Tk()
  window.title("Prey & Predator simulation")

  sim_frame = tk.LabelFrame(window, text="Simulation")
  sim_frame.grid(row=1, column=1, padx=10, pady=10, columnspan=5)
  grid_canvas = tk.Canvas(sim_frame, width=size16, height=size16, bg='ivory')
  grid_canvas.pack(padx=5, pady=5)
  refresh_canvas(grid_canvas, map)

  return window, grid_canvas
  
-génération des proies et prédateurs sur des espaces vides.

def generate_preys(map, size, N_pro, Apro):
  for  in range(N_pro):
    pos_x, pos_y = (None, None)
    while not pos_x and not pos_y or map[pos_y][pos_x] != 0:
      pos_x = r.randint(0, size - 1)
      pos_y = r.randint(0, size - 1)
    map[pos_y][pos_x] = Prey(A_pro)

  return map

def generate_predators(map, size, N_pre, A_pre, Epre):
  for  in range(N_pre):
    pos_x, pos_y = (None, None)
    while not pos_x and not pos_y or map[pos_y][pos_x] != 0:
      pos_x = r.randint(0, size - 1)
      pos_y = r.randint(0, size - 1)
    map[pos_y][pos_x] = Predator(A_pre, E_pre)

  return map
  
  -Déplacement des individus et création du Flair des prédateurs ainsi que de leurs déplacements en fonction
 
 def prey_move(y, x, map, size):
  ## Déplacement de la proie
  new_x, new_y = None, None
  timeout = 10

  while not new_x and not new_y and timeout > 0:
    timeout -= 1
    dir = r.randint(0, 7)
    if dir == 0 and (x > 0 and y > 0) and map[y-1][x-1] == 0:
      new_y, new_x = y-1, x-1
    if dir == 1 and y > 0 and map[y-1][x] == 0:
      new_y, new_x = y-1, x
    if dir == 2 and (x < size-1 and y > 0) and map[y-1][x+1] == 0:
      new_y, new_x = y-1, x+1
    if dir == 3 and x < size-1 and map[y][x+1] == 0:
      new_y, new_x = y, x+1
    if dir == 4 and (x < size-1 and y < size-1) and map[y+1][x+1] == 0:
      new_y, new_x = y+1, x+1
    if dir == 5 and y < size-1 and map[y+1][x] == 0:
      new_y, new_x = y+1, x
    if dir == 6 and (x > 0 and y < size-1) and map[y+1][x-1] == 0:
      new_y, new_x = y+1, x-1
    if dir == 7 and x > 0 and map[y][x-1] == 0:
      new_y, new_x = y, x-1

  if timeout == 0:
    return x, y
  return new_x, new_y
  
  while not new_x and not new_y and timeout > 0:
    timeout -= 1
    dir = r.randint(0, 7)
    if dir == 0 and (x > 0 and y > 0) and type(map[y-1][x-1]).name != 'Predator':
      new_y, new_x = y-1, x-1
    if dir == 1 and y > 0 and type(map[y-1][x]).name != 'Predator':
      new_y, new_x = y-1, x
    if dir == 2 and (x < size-1 and y > 0) and type(map[y-1][x+1]).name != 'Predator':
      new_y, new_x = y-1, x+1
    if dir == 3 and x < size-1 and type(map[y][x+1]).name != 'Predator':
      new_y, new_x = y, x+1
    if dir == 4 and (x < size-1 and y < size-1) and type(map[y+1][x+1]).name != 'Predator':
      new_y, new_x = y+1, x+1
    if dir == 5 and y < size-1 and type(map[y+1][x]).name != 'Predator':
      new_y, new_x = y+1, x
    if dir == 6 and (x > 0 and y < size-1) and type(map[y+1][x-1]).name != 'Predator':
      new_y, new_x = y+1, x-1
    if dir == 7 and x > 0 and type(map[y][x-1]).name != 'Predator':
      new_y, new_x = y, x-1

  if timeout == 0:
    return x, y
  def get_around(y, x, map, size):
  around = []
  s_y, s_x = 0 if y < (FLAIR+1) else y-FLAIR, 0 if x < (FLAIR+1) else x-FLAIR
  e_y, e_x = size-1 if y > size-(FLAIR+1) else y+FLAIR, size-1 if x > size-(FLAIR+1) else x+FLAIR

  for t_y in range(s_y, e_y+1):
    line = []
    for t_x in range(s_x, e_x+1):
      if map[t_y][t_x] == 0:
        line.append(0)
      elif t_y == y and t_x == x:
        line.append('X')
      elif type(map[t_y][t_x]).name == 'Prey':
        line.append(1)
      elif type(map[t_y][t_x]).name == 'Predator':
        line.append(2)
    around.append(line)

  return around

-Création des fonctions qui serviront à la reproduction des espèces.

def prey_birth(map, size, F_pro, A_pro):
  birth = 0

  while birth < F_pro:
    pos_x, pos_y = (None, None)
    while (not pos_x and not pos_y) or map[pos_y][pos_x] != 0:
      pos_x = r.randint(0, size - 1)
      pos_y = r.randint(0, size - 1)
    map[pos_y][pos_x] = Prey(A_pro)
    birth += 1

  return map

def preda_birth(map, size, A_pre, E_pre):
  pos_x, pos_y = (None, None)
  while (not pos_x and not pos_y) or map[pos_y][pos_x] != 0:
    pos_x = r.randint(0, size - 1)
    pos_y = r.randint(0, size - 1)
  map[pos_y][pos_x] = Predator(A_pre, E_pre)

  return map
  
  -Fonctions permettant le changement de couleur des cases en présence des différents individus , on considère être dans une prairie , la couleur verte est donc celle du sol.
  
  def refresh_canvas(canvas, map):
  prey, preda = 0, 0

  for y in range(len(map)):
    for x in range(len(map[y])):
      if map[y][x] == 0:
        canvas.create_rectangle(16x, 16y, 16(x+1), 16(y+1), outline='green', fill='green')
      elif type(map[y][x]).name == 'Prey':
        canvas.create_rectangle(16x, 16y, 16(x+1), 16(y+1), outline='blue', fill='blue')
        prey += 1
      elif type(map[y][x]).name == 'Predator':
        canvas.create_rectangle(16x, 16y, 16(x+1), 16(y+1), outline='orange', fill='orange')
        preda += 1

def print_around(around):
  for y in range(len(around)):
    for x in range(len(around[y])):
      if around[y][x] == 0:
        print("\033[0;102m \033[00m", end="")
      elif around[y][x] == 'X':
        print("\033[0;105m \033[00m", end="")
      elif around[y][x] == 1:
        print("\033[0;104m \033[00m", end="")
      elif around[y][x] == 2:
        print("\033[0;101m \033[00m", end="")
    print("\n",end="")
    
-On termine par créer les boutons sur l'interface et on les rends actifs . 

def add_buttons(window, canvas, map, size, N_pro, F_pro, A_pro, N_pre, A_pre, E_pre, E_repro):
  actions_frame = tk.LabelFrame(window, text="Actions")
  actions_frame.grid(row=2, column=1, padx=10, pady=10, columnspan=5)
  tk.Button(actions_frame, text="Prev").grid(row=1, column=1, padx=5, pady=5)
  tk.Button(actions_frame, text="Reset", command= lambda: reset(canvas, map, size, N_pro, A_pro, N_pre, A_pre, E_pre)).grid(row=1, column=2, pady=5)
  tk.Button(actions_frame, text="Next", command= lambda: next_step(map, size, canvas, F_pro, A_pro, A_pre, E_pre, E_repro)).grid(row=1, column=3, padx=5, pady=5)
def next_step(map, size, canvas, F_pro, A_pro, A_pre, E_pre, E_repro):
  map_c = np.array(map)

  for y in range(len(map_c)):
    for x in range(len(map_c[y])):


      if type(map_c[y][x]).name == 'Prey':

        prey = map_c[y][x]
        if prey.age == 0:

          map[y][x] = 0
        else:
          prey.age -= 1

          new_x, new_y = prey_move(y, x, map, size)
          map[y][x], map[new_y][new_x] = 0, prey

      elif type(map_c[y][x]).name == 'Predator':

        preda = map_c[y][x]
        if preda.age == 0:

          map[y][x] = 0
        elif preda.energy == 0:

          map[y][x] = 0
        else:
          if preda.energy == E_repro:

            preda_birth(map, size, A_pre, E_pre)
          preda.age -= 1
          preda.energy -= 1

          around = get_around(y, x, map, size)

          new_x, new_y = preda_move(y, x, map, size, around)
          if type(map[new_y][new_x]).name == 'Prey':

            preda.energy += MIAM
            map[y][x], map[new_y][new_x], map_c[new_y][new_x] = 0, preda, 0
          else:
            map[y][x], map[new_y][new_x] = 0, preda
map = prey_birth(map, size, F_pro, A_pro)
  refresh_canvas(canvas, map)

def reset(canvas, map, size, N_pro, A_pro, N_pre, A_pre, Epre):
  map = []
  for  in range(size):
    line = []
    for _ in range(size):
      line.append(0)
    map.append(line)
  map = generate_preys(map, size, N_pro, A_pro)
  map = generate_predators(map, size, N_pre, A_pre, E_pre)
  refresh_canvas(canvas, map)

if name == "main":
  map, size, N_pro, F_pro, A_pro, N_pre, A_pre, E_pre, E_repro = project_init()
  map = generate_preys(map, size, N_pro, A_pro)
  map = generate_predators(map, size, N_pre, A_pre, E_pre)

  window, grid = window_init(size, map)
  add_buttons(window, grid, map, size, N_pro, F_pro, A_pro, N_pre, A_pre, E_pre, E_repro)

  window.mainloop()

#!/usr/bin/python3

# (c) 2024 Daniel ou Jidé ou Boby ou l'ancien,
# ou arrêtez de me filer des noms qui me font passer
# pour un débile...

import os

# je sais ,jaurais pu trouver un autre nom
import pwel
from pwel import kolor

from data import lines, lines_hexa

# lines et lines_hexa : c'est le même texte, fastoche !
# cryptage symétrique ? comment ça marche ?
# je vais faire le curieux pour comprendre ce qui se passe

os.system("clear")

pwel.decrypte(lines); print("\n")

#pwel.crypte(lines)

pwel.read_all(lines_hexa)

print(f"\n{kolor.OKBLUE}Fin du Cryptage{kolor.ENDC}\n\n")
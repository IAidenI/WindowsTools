import time
import sys
import subprocess
import os
import importlib

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def is_module_installed(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

def library_install(packet):
    # Exécute la commande "pip install" en utilisant la fonction subprocess.run
    result = subprocess.run(["pip", "install", packet])

    # Vérifie si le téléchargement s'est déroulé avec succès
    if result.returncode != 0:
        print(f"Erreur lors du téléchargement du paquet '{packet}'.")
        print("Presser sur entrer pour continuer")
        input()
        sys.exit()

# Fonction qui attent le joueur, au lancement du .exe
def demande_permission_install(packet):
    print(f"Pour cette autoclicker vous allez avoir besoin de bibliothèque. ({packet})")
    print("Les installer ? y/n")
    while True:
        bib_choix = input(">")
        if bib_choix == 'y':
            library_install(packet)
            clear()
            break
        elif bib_choix == 'n':
            print("Dans ce cas impossible de lancer le programme.")
            time.sleep(2)
            sys.exit()
        else:
            print("Erreur de saisie")

# Déclaration des packets
packet_1 = "pyautogui"
packet_2 = "keyboard"
packet_3 = "pyfiglet"

# Vérifie si les packet sont installé
if not is_module_installed(packet_1):
    demande_permission_install(packet_1)

if not is_module_installed(packet_2):
    demande_permission_install(packet_2)

if not is_module_installed(packet_3):
    demande_permission_install(packet_3)


import pyautogui
import keyboard
import pyfiglet

# Fonction qui met en pause le programme lorsque f9 est pressé
def pause():
    print("Auto clicker en pause.")
    # Simule le relachement du clique de la souris
    pyautogui.mouseUp(x, y, button='left')

# Fonction qui lance le programme lorsque f8 est pressé
def start():
    print("Auto clicker est lancé.")
    # Simule le relachement du clique de la souris
    pyautogui.mouseDown(x, y, button='left')

# Fonction qui arrete le programme lorsque f7 est pressé
def stop():
    print("Auto clicker arreté.")
    # Simule le relachement du clique souris
    pyautogui.mouseUp(x, y, button='left')
    # Arret du programme
    sys.exit()


# Main
banner = pyfiglet.figlet_format("AutoClicker")
print(banner)
print("En attente d'un joueur.")
print("[f9] - Commencement de l'autoclicker.")
print("[f8] - Met en pause l'autoclicker")
print("[f7] - Quitter.")

# Obtient la position actuelle de la souris
x, y = pyautogui.position()
   
# Début de l'auto clicker
keyboard.add_hotkey('f9', pause)
keyboard.add_hotkey('f8', start)

keyboard.wait('f7')
stop()
    
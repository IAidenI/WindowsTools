import os
import sys
import pyfiglet

def parcours_dossier(path):
    fichiers = []
    dossiers = []

    for file_folder in os.listdir(path):
        element_path = os.path.join(path, file_folder)
        if os.path.isfile(element_path):
            if not file_folder.endswith(".srt"):
                fichiers.append(os.path.basename(element_path))
        elif os.path.isdir(element_path):
            dossiers.append(os.path.basename(element_path))
            sous_dossiers, sous_fichiers = parcours_dossier(element_path)
            fichiers += sous_fichiers
            dossiers += sous_dossiers
    return dossiers, fichiers

# Main
ascii_banner = pyfiglet.figlet_format("ScanFile")
print(ascii_banner)
print("Saisir le chemin d'accès à analyser:")
PATH_parent = input(">")

PATH_check = PATH_parent + '\\' + "list.txt"
try:
    list_fichier_dossier = os.listdir(PATH_parent)
except:
    print("[-] Le chemin d'accès est incorrect.")
    sys.exit()

print("\n[*] Analyse en cours ...")
dossiers, fichiers = parcours_dossier(PATH_parent)

lines = []
doublons = []
with open(PATH_check, 'w') as f:
    f.write(70 * "#" + "\n")
    for i in range(len(fichiers)):
        tab = (67 - len(fichiers[i])) * " "
        if fichiers[i] in lines:
            f.write(f"{i+1} - {fichiers[i]}{tab}# doublons\n")
            doublons.append(fichiers[i])
        else:
            f.write(f"{i+1} - {fichiers[i]}{tab}#\n")
        lines.append(fichiers[i])
    f.write(70 * "#" + "\n")
print(f"[*] {len(fichiers)} fichiers et {len(dossiers)} dossiers analysé.")

if len(doublons) == 0:
    print(f"[-] Aucun doublons trouvé.")
else:
    print(f"[*] {len(doublons)} doublons trouvé")
    print(f"Pour plus d'information voir {PATH_check}")
input("PRESS ENTER")

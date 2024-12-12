import sys
import os


print("[*] Recherche des réseaux sans fils enregistré...")
command = "netsh wlan show profiles"

try:
    output = os.popen(command).read()
    pattern = "Profil Tous les utilisateurs"
    if pattern not in output:
        print("[-] Votre pc n'as pas de carte réseaux sans fils ou n'as aucun réseau enregistré.")
        print("Press ENTER")
        input()
        sys.exit()

    lines = output.split('\n')
    netsh_profiles = [line.strip() for line in lines if line.strip()]

    profiles_list = ""
    for i in range(len(netsh_profiles)):
        if pattern in netsh_profiles[i]:
            profiles_list = netsh_profiles[i:]
            break

    for i in range(len(profiles_list)):
        for j in range(len(profiles_list[i])):
            if profiles_list[i][j] == ':':
                profiles_list[i] = profiles_list[i][j+1:].strip()
                break
except:
    print("[-] Une erreur est survenue dans la recherche.")

print("[+] Recherche réussi\n\nVoici la liste des réseaux enregistré:")

for profile in profiles_list:
    print("- " + profile)

print("\nSaissiez le réseau que vous voulez")
choix = input('>')
if choix not in profiles_list:
    print("[-] Ce réseau n'est pas présent.")
    print("Press ENTER")
    input()
    sys.exit()

payload = command + ' ' + choix + " key=clear"
output = os.popen(payload).read()
lines = output.split('\n')
list_propriete = [line.strip() for line in lines if line.strip()]

pattern = b'Contenu de la cl\xe2\x80\x9a            : '
for propriete in list_propriete:
    if pattern in bytes(propriete, 'utf-8'):
        print(f"[+] Clé trouvé pour {choix}: {bytes(propriete, 'utf-8').replace(pattern, b'').decode('utf-8')}")
        print("\nPress ENTER")
        input()
        sys.exit()
print("[-] Clé introuvable.")
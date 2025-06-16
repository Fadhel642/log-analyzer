# main.py — Analyse basique des logs SSH

# Ouvre le fichier log et lit les lignes
with open("sample_log.txt", "r") as file:
    lignes = file.readlines()

# Affiche toutes les lignes du fichier
print("Contenu du fichier log :")
for ligne in lignes:
    print(ligne.strip())

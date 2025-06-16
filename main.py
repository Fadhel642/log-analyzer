# main.py — Analyse des logs SSH : détection d'IP suspectes

with open("sample_log.txt", "r") as file:
    lignes = file.readlines()

print("Analyse des tentatives SSH :")
print("--------------------------------------")

echoues_par_ip = {}

for ligne in lignes:
    parts = ligne.split()

    if len(parts) < 11:
        continue  # ignore les lignes incomplètes

    date = parts[0]
    heure = parts[1]
    statut = parts[5]
    utilisateur = parts[8]
    ip = parts[10]

    print(f"{date} {heure} | Statut: {statut} | Utilisateur: {utilisateur} | IP: {ip}")

    if statut == "Failed":
        if ip not in echoues_par_ip:
            echoues_par_ip[ip] = 1
        else:
            echoues_par_ip[ip] += 1

print("\nIPs suspectes (3 échecs ou plus) :")
for ip, nb in echoues_par_ip.items():
    if nb >= 3:
        print(f"{ip} → {nb} tentatives échouées")

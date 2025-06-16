# Analyseur de journaux SSH

Projet Python pour analyser les fichiers de logs SSH et identifier les adresses IP suspectes.

## Objectif

Ce programme lit un fichier `sample_log.txt` contenant des logs de connexions SSH, et détecte les adresses IP qui ont échoué plusieurs fois à se connecter (3 fois ou plus).

## Fonctionnalités

- Lecture automatique d’un fichier de logs SSH
- Extraction des informations importantes :
  - Date et heure
  - Statut de connexion (Failed ou Accepted)
  - Nom d’utilisateur
  - Adresse IP
- Comptage des échecs de connexion par IP
- Affichage des IP suspectes (≥ 3 échecs)

## Exemple de sortie

```
2025-06-16 01:22:34 | Statut: Failed | Utilisateur: root  | IP: 192.168.1.10
2025-06-16 01:22:37 | Statut: Failed | Utilisateur: root  | IP: 192.168.1.10
2025-06-16 01:22:40 | Statut: Failed | Utilisateur: root  | IP: 192.168.1.10
2025-06-16 01:23:01 | Statut: Accepted | Utilisateur: admin | IP: 10.0.0.1
2025-06-16 02:00:00 | Statut: Failed | Utilisateur: user1 | IP: 203.0.113.50
2025-06-16 02:00:03 | Statut: Failed | Utilisateur: user1 | IP: 203.0.113.50

IPs suspectes (3 échecs ou plus) :
192.168.1.10 → 3 tentatives échouées
```
## Fichiers

- `main.py` : script principal d’analyse
- `sample_log.txt` : exemple de logs à analyser

## Remarque

Ce projet a été développé et testé dans l’environnement **Spyder (Python 3.8)**.


## Auteur

- Fadhel642 (GitHub)

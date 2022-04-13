# ProjetTransversal

Repo du PTC pour les scripts Python du Raspberry PI

---
Mettre ici le role de chaque script et ce qu'il va faire.

1) Acquisition d'image
2) Algorithmes de pathfinding
3) Algorithmes de plus court chemin
4) Faire une interface de contrôle
5) Traitement des acquisitions (analyse des données)
5) Lien entre STM32 et Raspberry PI ...

---

Transmission par port série

Etablissement de la connexion :
`Hello` envoyé par Raspberry, `Hello` envoyé par le STM32 en retour

Signaux de commande :

- `fwdXX` pour avancer de XX centimètres.
- `bwdXX` pour reculer de XX centimètres.
- `rotXX` pour tourner dans le sens horaire de XX0 degrés.

Transmission donnée des capteurs :

- `cX` pour indiquer transmission données de capteur (X indique le capteur).
- On réserve les n=32 prochains bits pour les données du capteur.

---

# Serveur Web / Scripts Python

## Commandes utilisées pour mettre en place le serveur

**Ne pas refaire quand on change de machine**

### Création serveur.

- `django-admin startproject mysite`
- `python3 manage.py migrate`

### Création app cmdRobot

`python3 manage.py startapp cmdRobot`.

### Gérer requêtes HTTP.

TODO.

### Configuration pour Templates, CSS, JS.

TODO.

## Packages nécessaires

- Django (framework)
- PySerial (communication par port série)

## Lancer le serveur

`python3 manage.py runserver`

---

# Parallélisme

## Objectifs

Processus:

- Gestionnaire de communications
- Serveur web
- Traitement / Interprétation / Prise décisions (Algos, Traitement signal)

Schéma:

```mermaid
flowchart LR
    id1([Queue])
    id2[/STM32/]
    
    Web--->|InstructionsManuelles|id1
    Traitements-->|Instructions|id1
    
    id1-->|Instructions|GestComm
    GestComm<-.->|Serial|id2
    
    GestComm-->|DonneesBrut|Traitements
    Traitements-->|DonneesAffichage|Web
```

# TODO

- Interface Web
  - Faire une requête http au propre avec du JS pour les boutons. Le body contiendra le bouton appuyé
  - Récupérer le contenu de la requête en backend et appeler la fonction du port série avec la direction donnée
- Parallélisme : cf. diagramme
  - Comment implémenter une Queue ?
  - Faire le squelette des process pour l'intégrer au projet (déjà fait pour serveur web)
  - Intégrer la communication entre process
- Interface série 
  - Refaire au propre
  - Coder proprement pour pouvoir modifier pour faire des tests et tout sans tout casser.
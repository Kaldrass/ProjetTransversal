# ProjetTransversal
Repo du PTC pour les scripts Python du Raspberry PI

---
Mettre ici le role de chaque script et ce qu'il va faire.  

1) Acquisition d'image 
2) Algorithmes de pathfinding
3) Algorithmes de plus court chemin
4) Faire une interface de contrôle
5) Traitement des acquisitions (analyse des données)
5) Lien entre STM32 et Raspberry PI 
...

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
TODO  
- Serveur web pour commandes manuelles
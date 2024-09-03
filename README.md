# Back-end Parking Management 

## Application de gestion de parking

### Features disponibles
- Obtenir un ticket de parking avec le numéro de la place
- Quitter le parking et libérer la place
- Récupérer toutes les places libres et occupées, avec leur numéro


## Installation 

**Requierments**

Docker doit être installé sur votre ordinateur

### Cloner le projet

```
git clone https://github.com/vincentverges/parking_management.git
```

### Installation de l'application 

Lancement des container
```
cd parking_management
docker compose up -d --build
```

Lancer les migrations pour la créations des tables dans la base de donnée

```
docker compose exec web python manage.py migrate
```

Création de 50 place places de parking occupées aléatoirement
```
docker compose exec web python manage.py create_parking_spots 50
```

Lancement des tests

```
docker compose exec web python manage.py test
```
# Gestion de Parking Backend

Ceci est l'application backend pour le système de gestion de parking, construite avec Django et Django REST Framework. Elle fournit des API pour la gestion des places de parking, la création de tickets et la libération des places.

## Fonctionnalités

- **API pour les places de parking** : Voir, créer, mettre à jour et supprimer des places de parking.
- **API pour les tickets de parking** : Créer des tickets pour occuper des places, et les libérer lorsque c'est terminé.

## Technologies utilisées

- **Django** : Framework web basé sur Python pour construire des applications web.
- **Django REST Framework** : Ensemble d'outils pour construire des API web.
- **PostgreSQL** : Système de gestion de bases de données relationnelles.
- **Test** : pour être intégré au tunnel CI avec Github Action
- **Docker** : facilité la mise en production

## Configuration du projet

### Cloner le projet

```bash
git clone https://github.com/vincentverges/parking_management.git
```

### Installation de l'application 

Lancement des containers :
```bash
cd parking_management
docker compose up -d --build
```

Lancer les migrations pour la créations des tables dans la base de donnée :

```bash
docker compose exec web python manage.py migrate
```

Création d'un nombre de place places de parking occupées aléatoirement, 20 dans cette exemple de commande :

```bash
docker compose exec web python manage.py create_parking_spots 20
```

Lancement des tests :

```bash
docker compose exec web python manage.py test
```
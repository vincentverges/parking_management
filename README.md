docker compose exec web python manage.py migrate
docker compose exec web python manage.py create_parking_spots 50
docker compose exec web python manage.py test

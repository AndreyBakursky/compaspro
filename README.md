1. Запустить в cmd docker-compose up
2. Делаем миграцию docker-compose exec web python manage.py migrate
3. Создаем суперпользователя для админки docker-compose exec web python manage.py createsuperuser
4. Перейти по http://127.0.0.1:8000/api/users/ или http://127.0.0.1:8000/admin/
5. Для запуска Django command использовать docker-compose exec web python manage.py create_users

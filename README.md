![workflow](https://github.com/Andrey-Vyshegorodskiy/foodgram-project-react/actions/workflows/main.yml/badge.svg)

# Foodgram
### Учебный проект

## Описание проекта

Проект о вкусной еде и рецептах. Сайт позволяет создавать рецепты, просматривать рецепты других и добавлять их в избранное. 
    Реализован следующий функционал: система аутентификации, создание/обновление и просмотр рецептов, добавление рецептов в избранное и список покупок, выгрузка списка покупок в txt формате, возможность подписки на авторов рецептов.

## Технологии

* Python

* Django

* Django Rest Framework

* Postgres

* Gunicorn

* Psycopg2-binary

* Nginx

* Docker

* docker-compose

# praktikum_new_diplom



sudo docker-compose exec backend python manage.py migrate --noinput

- Выполнить миграции:
```Bash
$ sudo docker-compose exec backend python manage.py migrate
```
- Собрать статику:
```Bash
$ sudo docker-compose exec backend python manage.py collectstatic --no-input
$ sudo docker-compose exec backend python manage.py createsuperuser
```
- Заполнить БД тестовыми записями:
```Bash
$ sudo docker-compose exec backend python manage.py load_data
```
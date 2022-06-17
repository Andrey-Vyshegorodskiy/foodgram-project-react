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

## Пользовательские роли

### Гость (неавторизованный пользователь)

Что могут делать неавторизованные пользователи:

- Создать аккаунт.
- Просматривать рецепты на главной.
- Просматривать отдельные страницы рецептов.
- Просматривать страницы пользователей.
- Фильтровать рецепты по тегам.

### Авторизованный пользователь

Что могут делать авторизованные пользователи:

- Входить в систему под своим логином и паролем.
- Выходить из системы (разлогиниваться).
- Менять свой пароль.
- Создавать/редактировать/удалять собственные рецепты
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингридиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

### Администратор

Администратор обладает всеми правами авторизованного пользователя. Плюс к этому он может:

- изменять пароль любого пользователя,
- создавать/блокировать/удалять аккаунты пользователей,
- редактировать/удалять любые рецепты,
- добавлять/удалять/редактировать ингредиенты.
- добавлять/удалять/редактировать теги.

### Ссылка на сайт:

http://130.193.54.104/

http://130.193.54.104/admin/

http://130.193.54.104/api/



### После развертывания проекта на удаленном сервере, обязательно выполнить: 
- Выполнить миграции:
```Bash
$ sudo docker-compose exec backend python manage.py migrate
```
- Собрать статику:
```Bash
$ sudo docker-compose exec backend python manage.py collectstatic --no-input
```
- Заполнить БД тестовыми записями:
```Bash
$ sudo docker-compose exec web python manage.py loaddata dump.json
```
- Создать суперпользователя:
```Bash
$ sudo docker-compose exec backend python manage.py createsuperuser
```


## Примеры

Примеры запросов по API:

- [GET] /api/users/ - Получить список всех пользователей.
- [POST] /api/users/ - Регистрация пользователя.
- [GET] /api/tags/ - Получить список всех тегов.
- [POST] /api/recipes/ - Создание рецепта.
- [GET] /api/recipes/download_shopping_cart/ - Скачать файл со списком покупок.
- [POST] /api/recipes/{id}/favorite/ - Добавить рецепт в избранное.
- [DEL] /api/users/{id}/subscribe/ - Отписаться от пользователя.
- [GET] /api/ingredients/ - Список ингредиентов с возможностью поиска по имени.


## Автор

- :white_check_mark: [Andrey-Vyshegorodskiy](https://github.com/Andrey-Vyshegorodskiy)

```

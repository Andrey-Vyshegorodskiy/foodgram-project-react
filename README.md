# praktikum_new_diplom


sudo docker-compose exec backend python manage.py migrate --noinput

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
$ sudo docker-compose exec backend python manage.py load_data
```
# FranchBook

Для работы требуется docker, node и bash. Их установить самостоятельно. Проект собран из: django, postgresql, docker, elastic. Статика собирается GULP

### Установка

Убедитесь, что у вас установлен [Docker](https://www.docker.com/).  
```sh
$ docker --version
```  
Все команды расположены в Makefile  
Установка
```sh
$ # Установка
$ make install # проверка работы контейнеров
$ docker ps
$ make recovery_db # Пробрасываем БД
$ # Done
```

Запуск. Сбор статики и запуск бэкенда делается в отдельных терминалах

Перед запуском надо в папке dockerfiles создать файл .env и заполнить его.

.env
```
POSTGRES_USER=
POSTGRES_DB=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
# PGDATA=/var/lib/postgresql/data/pgdata
C_FORCE_ROOT=true

DJANGO_DEBUG=True
DJANGO_SOCIAL_AUTH_FACEBOOK_KEY=
DJANGO_SOCIAL_AUTH_FACEBOOK_SECRET=
DJANGO_SOCIAL_AUTH_VK_OAUTH2_KEY=
DJANGO_SOCIAL_AUTH_VK_OAUTH2_SECRET=
DJANGO_SOCIAL_AUTH_TWITTER_KEY=
DJANGO_SOCIAL_AUTH_TWITTER_SECRET=

DJANGO_SMS_STREAM_TELECOM_LOGIN=
DJANGO_SMS_STREAM_TELECOM_PASSWORD=

DJANGO_ROBOKASSA_PASS_1=
DJANGO_ROBOKASSA_PASS_2=


DJANGO_AWS_ACCESS_KEY_ID=
DJANGO_AWS_SECRET_ACCESS_KEY=
DJANGO_AWS_S3_CUSTOM_DOMAIN=
DJANGO_AWS_STORAGE_BUCKET_NAME=

DJANGO_EMAIL_HOST=
DJANGO_EMAIL_PORT=
DJANGO_EMAIL_HOST_USER=
DJANGO_EMAIL_HOST_PASSWORD=

DJANGO_CACHES_DEFAULT_LOCATION=

DJANGO_CELERY_BROKER_URL=
DJANGO_CELERY_RESULT_BACKEND=

DJANGO_REDIS_HOST=
DJANGO_REDIS_PORT=
```

```sh
$ make run_django # run on localhost:8005
$ make stop_(all, django) # all-django, posgresql. django-django.
$ make migrate # makemigrations and migrate for django
$ make backup_db # create new backup db for path:/dockerfiles/backups/franchbook.backup.
$ make pip_install # pip install -r requirements.txt in django container
$ make recovery_db # Восстанавливает БД из бэкапа, сделанного командой backup_db
$ make build_static # Собирает статику в режиме watch
```
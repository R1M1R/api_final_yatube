# API для YaTube
### Описание
Благодаря этому проекту можно публиковать изменять удалять посты и загружать к ним фотографии, оставлять комментарии под постами и подписываться на понравившихся авторов.

Проект представляет собой API для проекта yatube.

Функционал: Авторизация по JWT токену

Сериализация данных для всех моделей проекта (Post, Comment, Group, Follow)

Обработка GET, POST, PATCH, PUT и DELETE запросов к базе данных проекта Yatube
### Технологии
Python, Django, DRF, Simple JWT.
### Библиотеки
```
Package                       Version
----------------------------- --------
asgiref                       3.7.2
atomicwrites                  1.4.1
attrs                         23.1.0
certifi                       2023.5.7
cffi                          1.15.1
charset-normalizer            2.0.12
colorama                      0.4.6
cryptography                  41.0.1
defusedxml                    0.7.1
Django                        3.2.16
django-cors-headers           4.0.0
django-filter                 23.2
django-templated-mail         1.1.1
djangorestframework           3.12.4
djangorestframework-simplejwt 5.2.2
djoser                        2.2.0
idna                          3.4
iniconfig                     2.0.0
oauthlib                      3.2.2
packaging                     23.1
Pillow                        9.3.0
pip                           23.1.2
pluggy                        0.13.1
py                            1.11.0
pycparser                     2.21
PyJWT                         2.1.0
pytest                        6.2.4
pytest-django                 4.4.0
pytest-pythonpath             0.7.3
python3-openid                3.2.0
pytz                          2023.3
requests                      2.26.0
requests-oauthlib             1.3.1
setuptools                    58.1.0
social-auth-app-django        5.2.0
social-auth-core              4.4.2
sqlparse                      0.4.4
toml                          0.10.2
typing_extensions             4.6.3
urllib3                       1.26.16
```
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:R1M1R/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Документация
Документация к API доступна по ссылке http://127.0.0.1:8000/redoc/ после запуска сервера разработчика

## **Примеры запросов**
```
GET /api/v1/posts/
```
**Образец ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
POST /api/v1/posts/
```
**Образец ответа**
```
}
    "text": "string",
    "image": "string",
    "group": 0
}
```
**Образец ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
PUT /api/v1/posts/{id}/
```
**Образец ответа**
```
{
    "text": "stringstring",
    "image": "string",
    "group": 0
}
```
**Образец ответа**
```
{
    "id": 0,
    "author": "stringstring",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
PATCH /api/v1/posts/{id}/
```
**Образец ответа**
```
{
    "text": "anotherstring"
}
```
**Образец ответа**
```
{
    "id": 0,
    "author": "stringstring",
    "text": "anotherstring",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
DELETE /api/v1/posts/{id}/
```
---
```
GET /api/v1/posts/{post_id}/comments/
```
**Образец ответа**
```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```
---
```
POST /api/v1/posts/{post_id}/comments/
```
**Образец ответа**
```
{
    "text": "string"
}
```
**Образец ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
---
```
POST /api/v1/jwt/create/
```
**Образец ответа**
```
{
    "username": "string",
    "password": "string"
}
```
**Образец ответа**
```
{
    "refresh": "string",
    "access": "string"
}
```

### Автор:

 - [Усеинов Эмир](https://github.com/R1M1R)

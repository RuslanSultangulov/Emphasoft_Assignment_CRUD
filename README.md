# Emphasoft_Assignment_CRUD
 
Реализовать CRUD для юзеров с токен-аутентификацией. Пример - https://emphasoft-test-assignment.herokuapp.com/swagger/.

# Стек технологий/библиотек

- Django
- Django REST Framework
- Flake8 в качестве линтера
- HTTPie в качестве HTTP-клиента

# Эндпоинты и примеры запросов, используя HTTPie

- /api-token-auth/ - эндпоинт для получения токена для аутентификации.
Пример запроса: 
http POST http://localhost:8000/api-token-auth/ username=user password=ejhwesk23

Пример ответа (body): 
{
    "token": "39edac15fff8e8c6ccbb1493c3cace35f7778119"
}

- /api/users - эндпоинт для просмотра всех пользователей или для создания нового пользователя.

Пример GET-запроса:
http GET http://localhost:8000/api/users/ "Authorization: Token 39edac15fff8e8c6ccbb1493c3cace35f7778119"

Пример ответа (body):
[
    {
        "first_name": "first_name",
        "id": 1,
        "is_active": true,
        "is_superuser": false,
        "last_login": "2021-06-14T14:41:56Z",
        "last_name": "last_name",
        "username": "first_user"
    },
    {
        "first_name": "first_name",
        "id": 2,
        "is_active": true,
        "is_superuser": false,
        "last_login": null,
        "last_name": "last_name",
        "username": "user"
    },
]

Пример POST-запроса:
http POST http://localhost:8000/api/users/ "Authorization: Token 39edac15fff8e8c6ccbb1493c3cace35f7778119" username=user3 first_name=first_name last_name=last_name password=password is_active=true last_login=""

Пример ответа (body):
{
    "first_name": "first_name",
    "is_active": true,
    "last_name": "last_name",
    "password": "password",
    "username": "user3"
}

- /api/v1/users/{id}/ - эндпоинт для просмотра атрибутов, редактирования или удаления конкретного пользователя из БД.

Пример GET-запроса:
http GET http://localhost:8000/api/users/2 "Authorization: Token 39edac15fff8e8c6ccbb1493c3cace35f7778119"

Пример ответа (body):
{
    "first_name": "first_name",
    "id": 2,
    "is_active": true,
    "is_superuser": false,
    "last_login": null,
    "last_name": "last_name",
    "username": "user"
}

Пример PUT-запроса:
http PUT http://localhost:8000/api/users/2 "Authorization: Token 39edac15fff8e8c6ccbb1493c3cace35f7778119" username=new_username first_name=new_first_name last_name=new_last_name password=new_password is_active=true last_login=2021-06-14T14:47:49.237122Z

Пример ответа (body):
{
    "first_name": "new_first_name",
    "is_active": true,
    "last_name": "new_last_name",
    "password": "new_password",
    "username": "new_username"
}


Пример PATCH-запроса:
http PATCH http://localhost:8000/api/users/2 "Authorization: Token 39edac15fff8e8c6ccbb1493c3cace35f7778119" username=patched_username first_name=patched_first_name last_name=patched_last_name

Пример ответа (body):
{
    "first_name": "patched_first_name",
    "is_active": true,
    "last_name": "patched_last_name",
    "password": "new_password",
    "username": "patched_username"
}

Пример DELETE-запроса:
http PATCH http://localhost:8000/api/users/2 "Authorization: Token 39edac15fff8e8c6ccbb1493c3cace35f7778119"

Код ответа - 204 No Content.

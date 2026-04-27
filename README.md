[![Main Kittygram workflow](https://github.com/Sergey-A-Dmitriev/kittygram_final/actions/workflows/main.yml/badge.svg)](https://github.com/Sergey-A-Dmitriev/kittygram_final/actions/workflows/main.yml)

# Kittygram + API

## Описание проекта

**Kittygram** — REST API для платформы, агрегирующей фото всяких котиков. Проект позволяет управлять карточками  котиков и их достижениями. Пользователи могут оставлять фотографии любых котов.

## Пользовательские роли

**User:** Авторизованный пользователь: публикация фотографий, добавление достижений, редактирование и удаление собственных материалов.

**Admin:** Полный контроль, включая управление проектом, а также назначение ролей другим пользователям.

**Superuser Django:** Все права admin + технические права Django.

## Технологии

- Python 3.10+

- Django 5.1+

- Django REST Framework

- djangorestframework TokenAuthentication


## Endpoints

### Auth

| Endpoint                            | Метод  | Описание                               | Права доступа               |
|-------------------------------------|--------|----------------------------------------|-----------------------------|
| `/api/token/login/`                 | POST   | Login, возвращает токен аутентификации | Доступно без токена         |
| `/api/token/logout/`                | POST   | Logout, выход из системы               | Авторизованный пользователь |
| `/api/users/activation/`            | POST   | Активация аккаунта                     | При наличии токена          |
| `/api/users/resend_activation/`     | POST   | Повторная отправка письма активации    | При наличии токена          |
| `/api/users/reset_password/`        | POST   | Запрос сброса пароля                   | Не требует аутентификации   |
| `/api/users/reset_password_confirm/`| POST   | Подтверждение нового пароля            | Не требует аутентификации   |
| `/api/users/reset_username/`        | POST   | Запрос сброса username                 | Не требует аутентификации   |
| `/api/users/reset_username_confirm/`| POST   | Подтверждение нового username          | Не требует аутентификации   |
| `/api/users/set_username/`          | POST   | Изменение username                     | Авторизованный пользователь |
| `/api/users/set_password/`          | POST   | Изменение пароля                       | Авторизованный пользователь |

### Users

| Endpoint                  | Метод  | Описание                               | Права доступа               |
|---------------------------|--------|----------------------------------------|-----------------------------|
| `/api/users/`             | GET    | Получение списка всех пользователей    | Администратор               |
| `/api/users/`             | POST   | Добавление пользователя                | Администратор               |
| `/api/users/me/`          | GET    | Получение данных своего профиля        | Авторизованный пользователь |
| `/api/users/me/`          | PUT    | Полная замена своего профиля           | Авторизованный пользователь |
| `/api/users/me/`          | PATCH  | Частичная корректировка своего профиля | Авторизованный пользователь |
| `/api/users/me/`          | DELETE | Удаление своего профиля                | Авторизованный пользователь |
| `/api/users/{id}/`        | GET    | Получение профиля пользователя         | Администратор               |
| `/api/users/{id}/`        | PUT    | Полная замена профиля пользователя     | Администратор               |
| `/api/users/{id}/`        | PATCH  | Редактирование профиля пользователя    | Администратор               |
| `/api/users/{id}/`        | DELETE | Удаление профиля пользователя          | Администратор               |


### Cats

| Endpoint                  | Метод  | Описание                        | Права доступа               |
|---------------------------|--------|---------------------------------|-----------------------------|
| `/api/cats/`              | GET    | Получение списка всех котов     | Авторизованный пользователь |
| `/api/cats/`              | POST   | Добавление нового кота          | Авторизованный пользователь |
| `/api/cats/{id}/`         | GET    | Получение записи кота           | Автор                       |
| `/api/cats/{id}/`         | PUT    | Полная замена записи кота       | Автор                       |
| `/api/cats/{id}/`         | PATCH  | Редактирование элементов записи | Автор                       |
| `/api/cats/{id}/`         | DELETE | Удаление записи кота            | Автор                       |

### Achievements

| Endpoint                  | Метод  | Описание                        | Права доступа               |
|---------------------------|--------|---------------------------------|-----------------------------|
| `/api/achievements/`      | GET    | Получить список всех достижений | Авторизованный пользователь |
| `/api/achievements/`      | POST   | Добавить достижение             | Авторизованный пользователь | 
| `/api/achievements/{id}/` | GET    | Получить запись достижения      | Авторизованный пользователь |
| `/api/achievements/{id}/` | PUT    | Заменить запись достижения      | Авторизованный пользователь |
| `/api/achievements/{id}/` | PATCH  | Редактировать запись достижения | Авторизованный пользователь |
| `/api/achievements/{id}/` | DELETE | Удалить запись достижения       | Авторизованный пользователь |


## Локальное развертывание

**Клонирование репозитория:**

```bash

git clone https://github.com/Sergey-A-Dmitriev/kittygram_final.git
cd <название_директории_проекта>
```

**Создание и активация виртуального окружения:**

```bash

python -m venv venv

source venv/bin/activate  # Для Linux/macOS

source venv/Scripts/activate    # Для Windows
```

**Установка зависимостей:**

```bash

pip install -r requirements.txt
```

**Подготовка базы данных:**

```bash

python manage.py migrate
```

**Создание суперпользователя (опционально):**

```bash
python manage.py createsuperuser
```

**Запуск сервера:**

```bash

python manage.py runserver
```

Сервер будет доступен по адресу `http://127.0.0.1:8000/.`

## Примеры использования API

### Регистрация пользователя
```
POST /api/token/login/
{
    "username": "john_doe",
    "password": "securePass123"
}
```
Ответ:

```
{}JSON
{
    "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Получение данных своей учетной записи
```
GET /api/users/me/
```
Ответ:
```
{}JSON
{
    "email": "",
    "id": 5,
    "username": "newman"
}
```

### Котики
```
Получение всех котиков
GET /api/cats/
```
Ответ:
```
{}JSON
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4, 
            "name": "Сибиряк",
            "color": "white",
            "birth_year": 2015,
            "achievements": [],
            "owner": 3,
            "age": 11,
            "image": "http://kittygramer.ru/media/cats/images/temp_ZVOm6Fd.jpeg",
            "image_url": "/media/cats/images/temp_ZVOm6Fd.jpeg"
        },
        {
            "id": 3,
            "name": "Зюзя",
            "color": "white",
            "birth_year": 2024,
            "achievements": [
                {
                    "id": 1,
                    "achievement_name": "Спит как сурок!"
                }
            ],
            "owner": 1,
            "age": 2,
            "image": "http://kittygramer.ru/media/cats/images/temp_GQ0ydb2.jpeg",
            "image_url": "/media/cats/images/temp_GQ0ydb2.jpeg"
        },
        {
            "id": 2,
            "name": "Пух",
            "color": "white",
            "birth_year": 2024,
            "achievements": [
                {
                    "id": 1,
                    "achievement_name": "Спит как сурок!"
                },
                {
                    "id": 3,
                    "achievement_name": "Уснул в лотке"
                }
            ],
            "owner": 1,
            "age": 2,
            "image": "http://kittygramer.ru/media/cats/images/temp.jpeg",
            "image_url": "/media/cats/images/temp.jpeg"
        }
    ]
}
```

### Достижения
```
Получение всех достижений
GET /api/achievements/
```
Ответ:
```
{}JSON
[
    {
        "id": 1,
        "achievement_name": "Спит как сурок!"
    },
    {
        "id": 2,
        "achievement_name": "34543"
    },
    {
        "id": 3,
        "achievement_name": "Уснул в лотке"
    }
]
```
```
Получение выбранного достижения
GET /api/achievements/{id}/
```
Ответ:
```
{}JSON
{
    "id": 1,
    "achievement_name": "Спит как сурок!"
}
```
```
Создание нового достижения
POST /api/achievements/ 
{
    "achievement_name": "Ловит мышей"
}
```
Ответ:
```
{}JSON
{
    "id": 4,
    "achievement_name": "Ловит мышей"
}
```

## Автор

[Дмитриев Сергей](https://github.com/Sergey-A-Dmitriev)

# Финальный проект по API
# API на базе Django REST Framework

### Как установить:
-настройте виртуальное окружение
    ```
    python3 -m venv venv_name
    ```
-установите необходимые зависимости
    ```
    pip install -r requirements.txt
    ```
- запустите проект
    ```
    python manage.py runserver
    ```


### Примеры запроса к API:
```
/api/v1/posts/   (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>   (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments  (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments/<id>  (GET, POST, PUT, PATCH, DELETE)
/api/v1/group/ (GET, POST)
/api/v1/follow/  (GET, POST)

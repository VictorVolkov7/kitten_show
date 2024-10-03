# [The Kitten Show](https://github.com/VictorVolkov7/kitten_show)


## Оглавление:

- [Технологии](#технологии)
- [Описание проекта](#Описание-проекта)
- [Права пользователей](#Права-пользователей)
- [Установка и запуск проекта](#установка-и-запуск-проекта)
- [Использование](#Использование)
- [Автор](#Автор)


## Технологии:

- Python 3.12

С использованием библиотек/фреймворков:
- Django 5.0.7
- Django REST framework 3.15.2
- drf-spectacular 0.27.2
- PostgreSQL


## Описание проекта:

Python сервис,
предоставляющий REST API интерфейс с методами:
- управления котятами;
- системой отзывов;
- регистрации и аутентификацией пользователей;

Backend-составляющая для выставки котят также имеет готовый Django admin интерфейсом. 


## Права пользователей:

### Авторизованный пользователь может:

Зарегистрированные пользователи могут регистрировать своих котят, редактировать данные своих котят,
а также снимать с выставки. Каждый пользователь может ставить оценки любым котятам, представленным на выставке.


## Установка и запуск проекта

### Запуск проекта:

* Форкните/Клонируйте репозиторий и перейдите в него:
```
git clone https://github.com/VictorVolkov7/kitten_show
```

* Создайте и активируйте виртуальное окружение:
```
poetry shell
```
Установите зависимости:
```
poetry install
```

* Создайте **.env** файл в корневой папке проекта. В нем должны быть указаны переменные из файла **.env.sample**.
```ini
# Django settings
DJANGO_SECRET_KEY=django_secret_key

# PostgreSQL settings
POSTGRES_DB=db_name
POSTGRES_USER=psql_username
POSTGRES_PASSWORD=psql_password
POSTGRES_HOST=local_ip
POSTGRES_PORT=port_for_db

# Superuser creation
SU_EMAIL=your_email@gmail.com
SU_PASSWORD=your_password
```

* Создайте и примените миграции:
```
python manage.py makemigrations
python manage.py migrate
```

* Воспользуйтесь командой для установки русского языка:
```
django-admin compilemessages
```

* ЗАПУСК BACKEND-ЧАСТИ: Запустите сервер:

`python manage.py runserver` или настройте запуск Django сервера в настройках.


Таким образом можно работать с backend-частью локально для отладки.

После запуска сервера. Вы сможете перейти на сайт с документацией http://127.0.0.1:8000/api/schema/swagger-ui/ или
http://127.0.0.1:8000/api/schema/redoc/ (если сервер запущен локально), и начать пользоваться всеми API методами проекта. 

Также вы можете схему данных .yaml файлом по адресу http://127.0.0.1:8000/api/schema/ (если сервер запущен локально).

### Либо с помощью Docker
* Измените файл **.env** в корневой папке проекта, заменив значение в строчке **"POSTGRES_HOST"** на Ваше название 
контейнера с базой данных:
```ini
# Django settings
DJANGO_SECRET_KEY=django_secret_key

# PostgreSQL settings
POSTGRES_DB=db_name
POSTGRES_USER=psql_username
POSTGRES_PASSWORD=psql_password
POSTGRES_HOST=container_name(default:"db")
POSTGRES_PORT=port_for_db

# Superuser creation
SU_EMAIL=your_email@gmail.com
SU_PASSWORD=your_password
```

* ЗАПУСК BACKEND-ЧАСТИ:: Воспользуйтесь командами:
```
docker compose build (для создания оптимального билда проекта).

docker compose up -d (для запуска docker compose контейнера (флаг -d запуск в фоновом режиме)).
```
Сервис будет доступен по вашему локальному адресу с портом 8000. Документация **(см. выше)**.

## Использование
* Можно заполнить базу данных тестовыми данными командой `python manage.py load_fixture` из файлов фикстур 
(лучше сначала заполнить фикстурами, потом использовать команду для создания суперпользователя).
* На проекте реализована регистрация новых пользователей через API.
Также есть команда для создания суперпользователя `python manage.py csu` с данными из .env файла
* Поиск котят по породе происходит по ID породы. Пример запроса: http://127.0.0.1:8000/api/kittens/?breed=1
* Запуск всех тестов командой `pytest tests`. Проверка покрытия `pytest --cov`

*При использовании сервиса через Docker надо сначала узнать ID бэкенд контейнера командой `docker ps -a`, 
далее зайти в контейнер с оболочкой bash и применить команды **(см. выше)**.


* Тестовые данные для проверки API можно взять в папке **fixtures** в корневой папке проекта.


## Автор
[Volkov Victor](https://github.com/VictorVolkov7/)
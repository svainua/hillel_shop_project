## Setup the environment

```sh
python -m venv venv

## Unix
source venv/bin/activate
# Windows
\venv\Scripts\activate.bat

pip install -r requirements.txt
```

## Setup the database

```sh
python manage.py migrate
```

## Run the application

```sh
python manage.py runserver
```

# Tools

## Local

**Operating System**: Windows 10

**Editor**: Visual Studio Code

## Server

**Backend**: Django

**API**: REST (upgrade to GraphQL someday)

**Hosting**: Heroku

**Authentication**: JWT

## Client

**Frontend**: React SPA via React Router

**Style**: Bootstrap

# Setup

## [Dakota Lillie's Tutorial](https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a)

##### cmd

```powershell
cd Mumbo-Scrumbo
python -m venv env
env\Scripts\activate
```

##### env

```powershell
pip install django
pip install djangorestframework
pip install djangorestframework-jwt
pip install django-cors-headers
django-admin startproject server
```

##### server/settings.py

Make [these changes](https://gist.github.com/dakotalillie/146d94b3e2a50cc565bf69bde6ad495e#file-settings-py).

##### server/urls.py

Make [these changes](https://gist.github.com/dakotalillie/43ae67163db03825ef04d236730ec62e#file-urls-py).

##### env

```powershell
cd server
python manage.py migrate
```

###### testing

```powershell
python manage.py createsuperuser
# fields can be whatever you want... it won't make it into production anyway
python manage.py runserver
```

Open https://localhost:8000/token-auth/ and verify that the credentials for the superuser you created work.

##### env

```powershell
python manage.py startapp core
```

##### server/settings.py

Make [these changes](https://gist.github.com/dakotalillie/12c8351d96f37cf29b630c7d5d8e67be#file-settings-py).

##### setup Accounts backend

Here I deviate from the tutorial and make [these changes](https://github.com/xujustinj/Mumbo-Scrumbo/commit/a5bc845e1f3fd1dc2a3de9452029186db5e147c0) instead.

# Resources

[Django & React: JWT Authentication | by Dakota Lillie | Medium](https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a)

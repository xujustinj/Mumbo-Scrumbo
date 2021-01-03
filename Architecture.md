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

##### cmd

```powershell
cd Mumbo-Scrumbo
python -m venv env
env\Scripts\activate
```

##### env

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-jwt
pip install django-cors-headers
django-admin startproject server
cd server
```

# Resources

[Django & React: JWT Authentication | by Dakota Lillie | Medium](https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a)
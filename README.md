# Django Bookstore
Online bookstore made with Django

## Prerequisites:
- Python
- Django
- PostgreSQL
- Docker

## Installation
Clone the repo:
```zsh
$ git clone git@github.com:Ersain/django-bookstore.git
```
Build the project:
```zsh
$ cd django-bookstore && docker build .
```
Run it with `docker-compose`:
```zsh
$ docker-compose up -d
```
Go to http://127.0.0.1:8000/

## Attention
Unfortunately, the dependencies of the project may be broken and fail to build a wheel while building (I suspect it is due to Pipfile). Thus, it cannot be launched via Docker. I am going to fix this in near feature, pull requests are welcome

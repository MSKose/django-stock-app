<!-- Please update value in the {}  -->

<h1 align="center">Django Stock App</h1>


<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Stack & Tools](#stack)
- [Notes](#notes)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

This is a back-end stock-app project made with Django DRF. I have used different tools to develop this project, including drf-yasg, django toolbar, and django rest auth

<p align="center">
  <img src="https://user-images.githubusercontent.com/98649983/194851648-3e22780b-7e5c-481f-aabc-facc261b485b.gif">
</p>

<h2 id="stack">Stack & Tools</h2>

- Django
- Django Rest Framework
- Django Nested Admin
- Django Filter
- PostgreSQL
- Django Debug Toolbar
- drf-yasg (Swagger generator)
- dj-rest-auth

## Notes
### Entity Relationship Diagram

![Entity Relationship Diagram](https://user-images.githubusercontent.com/98649983/194851017-083393e4-53ef-425d-869c-903d8515fdaa.jpg)

### Project info

#### User Roles (You can set it from the admin panel.)

  - Manager:
    - Authorizes all CRUD operations in Stock App 
  - Product_Manager:
    - Authorizes all CRUD operations in Category, Brand, Firm, Product tables
  - Finance:
    - Authorizes all CRUD operations in Transaction table and read-only for other tables
  - Read_Only:
    - Authorized for read-only operations in all tables

#### Transactions Operations

  - Transaction field determines the type of stock object. 
  - If the transaction is 'IN', stock of product object is recalculating.
  - If the transaction is 'OUT' we are checking stock of product in Product table if there is enough stock. If there isn't enough stock in product we are raising ValidationError; otherwise, we are recalculating the stock of product object.
  - Price_total field is read_only field and we are calculating this value with quantity and price fields.
  - All views have filter and search features. 
  - In addition to the filters in category views we also have nested serializer which shows which product belongs to which categories. 


## Project Structure

```bash
.──── django-flight-app (repo)
│
├── README.md
├── manage.py
├── requirements.txt
├── main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── db.sqlite3
│   ├── settings
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── account
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── stock
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── permissions.py
    ├── serializers.py
    ├── signals.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/MSKose/django-stock-app

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Add the following to your .env file
    SECRET_KEY=<yourSecretKeyHere>
    DEBUG=True # switch to True when in production
    ENV_NAME=dev # switch to prod when in production
    DEBUG=True 
    SQL_DATABASE=<yourDatabaseProjectName>
    SQL_USER=<yourDatabaseUsername> 
    SQL_PASSWORD=<yourDatabasePassword>
    SQL_HOST=localhost 
    SQL_PORT=5432

# Run the app
    $ python manage.py runserver
```

## Contact

- [Linkedin](https://www.linkedin.com/in/mustafa-kose-linked/)
- [GitHub](https://github.com/MSKose)
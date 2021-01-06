# Dessert API
A REST API for Dessert Recipes made with Django REST framework


## Description

Dessert API is a REST API which holds the data of desserts and recipes.This API is made for an android app D'Zone Dessert Recipes(For Experimental Purposes Only).An API consits of 2 Databases which generates a json format of the database.The json format which is posted on localhost will be retrived to android application and the data will be displayed as dynamic content in android application.The API is still under development.

## Specifications

- REST API Framework : Django REST Framework
- Language : Python 
- Database Management Framework : Postgresql
- Databases : Categories DB, Desserts DB

## Requirements

- Python 3.x Installed
- Django 3.0.2 
- Postgresql
- PgAdmin
- Psycopg2 (PostgresqlDB to Django class connector library)

## Instructions

- Unzip the downloaded file
- Go to Base python installation directory and run command 'pip3 install -r requirments.txt' and wait for installation
- Change terminal directory to project directory.
- Run command 'python manage.py runserver'.
- open 'localhost:8000' in web browser.
- Retrive Data Through Postman (Optional)

## Adding Data to Database

- Go to Django Admin Panel('localhost:8000/admin')
- Login with username and password described in details.txt.
- Fill the entries in the fields that needs to be added or updated.
- Save and Restart the Server.

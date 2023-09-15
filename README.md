
# Voice Interactive Login Page using Python And MySQL

It is a voice Interactive login page, that supports three features - 1.)Login
2.) SignUP 3.)Change Pasword

The username and password are stored in a database "users".
In the database we have a table "login_details".

## Documentation
    Database Creation Command:
        create database users;
    
    Table Creation:
        create table login_details(user_id varchar(20) Primary Key, password varchar(20) Primary Key)

    Python Modules used:
    -> pyttsx - https://pypi.org/project/pyttsx3/ - for voice output
    -> rich - https://pypi.org/project/rich/ - for colored terminal output
    -> mysql-connector-python -https://pypi.org/project/mysql-connector-python/ - for database connectivity

    
    

## Installation

-> First install all the required modules, then create the database and tables.
    
## Features

- Login with database verification
- signup as a new user
- Colored terminal output and voice interactivity
- Database connectivity


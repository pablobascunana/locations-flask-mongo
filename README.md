# Locations API

Locations is a RestFull API that connect with MongoDB and allows to create users, get, save and delete
locations associated to it. The content of this project is only for educational purposes.

## How to run this project

* This project use **Pipenv**. You can read the docs [here](https://pipenv-es.readthedocs.io/es/latest/).
* You need to modify the database connection inside **.env** with your database credentials and the database name.
The collections will be created automatically.
* The unit test are written with **Pytest**. You can run a test file with the following command
```
pytest filename.py
```
or the whole test collection with 

```
pytest *
```
You should run these commands in the terminal and inside the test folder.
* When you run the project you can visit `http://localhost:5000/apidocs` to view the swagger documentation.

## How to use Locations API

* Locations API can be consumed by the following
[repository](https://github.com/pablobascunana/locations-vue2) that is a web page created with vue2 that allow you
to create users, get, save and delete locations.
* Also you can consume the API using Postman importing the following
[collection](https://www.getpostman.com/collections/707f21960956d6df9d11).

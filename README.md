# Python SQL

Instalar lib

    $ sudo apt-get install libpq-dev python-psycopg2

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 env
    $ cd env
    $ source bin/activate

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

En Windows:

    > env\Scripts\activate.bat

---

Fuentes:

+ https://github.com/kennethreitz/records
+ http://initd.org/psycopg/docs/module.html
+ https://github.com/pepeul1191/python-bottle-postgres-quinua
+ http://zetcode.com/python/psycopg2/
covid19.quarantine
==================

Dashboarding of quarantine center capacity & utilization

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^


* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser


Running
----------

The following details how to deploy this application.



Database setting
^^^^^^^^^^^^^^^^

Postgres container with GIS support

```
docker run --name=postgis -d -e POSTGRES_USER=<username> -e POSTGRES_PASS=<password> -e POSTGRES_DBNAME=<password> -p 5432:5432 kartoza/postgis:9.6-2.4
```

Export the database URL in your shell


```
export DATABASE_URL="postgres://covid19:quarantine@localhost:5432/covid19_quarantine"
```
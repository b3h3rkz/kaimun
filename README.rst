kaimun
======

Kaimun App

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up the project

Make sure to have the following on your host:

* virtualenv;

* pip;


* PostgreSQL.

^^^^^^^^^^^^^^^^^^^^^

* create a database called **kaimun**

* clone this repository ::

    $ git clone https://github.com/b3h3rkz/kaimun.git


* create and activate a virtualenv


* Run install dependencies ::
    $ pip install -r requirements/local.txt


* create a file **keys.py** in the config.settings package and add the following constants to it ::


    MONEY_RAVE_API_KEY = "key"
    MONEY_RAVE_API_SECRET = "key"
    NAIRA_WALLET_LOCK = "password"
    CEDIS_WALLET_LOCK = "password"

    FLW_API_KEY = "FLWPUBK-=ere-X"
    FLW_API_SECRET = "FLWSECK--X"



* Apply migrations ::
    $ python manage.py migrate


* See the application being served through Django development server::
    $ python manage.py runserver 0.0.0.0:8000

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest







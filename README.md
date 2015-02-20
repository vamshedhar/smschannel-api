SMS Channel API
==============================

API of sms portal of IIT Roorkee Saharanpur Campus. Developed by IMG, IIT Roorkee-Saharanpur Campus

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv

First make sure to create and activate a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt

You can now run the ``runserver`` command::

    $ python manage.py runserver

The base app will run but you'll need to carry out a few steps to make it functional.

Create database by running ``syncdb`` command. It will request you to create a superuser. Please proceed creating a superuser account.

	$ python manage.py syncdb

Finally for working with django-uuid you need to apply this [fix](https://github.com/dcramer/django-uuidfield/pull/22/files).

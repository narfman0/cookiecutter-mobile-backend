{{ cookiecutter.project_slug }}
==============

Django based AWS lambda friendly mobile backend framework. Includes rest framework{% if cookiecutter.use_bootstrap == 'y' %}, bootstrap3{% endif %}

Usage
-----

Dev:

#. Optional: Create virtualenv and source :code:`virtualenv venv; source venv/bin/activate`
#. Install requirements :code:`pip install -r requirements.txt`
#. Apply migrations :code:`./manage.py migrate`
#. Create user :code:`./manage.py createsuperuser`
#. Run dev server :code:`./manage.py runserver`
#. Navigate in browser to :code:`localhost:8000` log in etc
#. Optional: navigate to :code:`localhost:8000/api` Congrats!

Staging (note prod is the same, but substitute 'prod' for 'staging'):

#. Optional: Create virtualenv and source :code:`virtualenv venv; source venv/bin/activate`
#. Install requirements :code:`pip install -r requirements.txt`
#. Apply migrations :code:`./manage.py migrate --settings {{ cookiecutter.project_slug }}.settings.staging`
#. Collectstatic :code:`./manage.py collectstatic --settings {{ cookiecutter.project_slug }}.settings.staging`
#. Create user :code:`./manage.py createsuperuser --settings {{ cookiecutter.project_slug }}.settings.staging`
#. Ensure CORS is enabled for the s3 bucket (aws / s3 / bucket / properties / permissions / edit CORS / save)
#. Deploy via zappa::

    zappa deploy staging

API Notes

* For individual pages, you may append param detail=True to get a `detail` attribute with all the html
* For individual pages, you may append param absolute=True to ensure paths are absolute (s3 should make
  this unimportant)

License
-------

Copyright (c) 2016 {{ cookiecutter.author_name }}

See included LICENSE for licensing information

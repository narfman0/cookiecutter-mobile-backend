{{ cookiecutter.project_slug }}
==============

Django based AWS lambda friendly mobile backend framework. Includes rest framework, bootstrap3

Usage
-----

#. Ensure aws/boto credentials are set up with proper access for dev e.g. `~/.aws/credentials`
#. Set up database(s) and migrate with `./manage.py migrate`
#. Create user `./manage.py createsuperuser`
#. Run dev server `./manage.py runserver`
#. Navigate in browser to `localhost:8000` log in etc. Maybe navigate to `localhost:8000/api` Congrats!
#. Note: for staging/prod, add the `--settings` arg like: `./manage.py createsuperuser --settings mobile_backend.settings.staging`
#. After making it your own^tm, deploy via zappa::

    zappa deploy staging

License
-------

Copyright (c) 2016 {{ cookiecutter.author_name }}

See included LICENSE for licensing information


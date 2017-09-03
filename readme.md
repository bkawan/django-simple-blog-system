create database for postgres and change the necessary configuration in ```simple-blog/config/settings/env.py```
Then 

create virtualenv for python3

``$ virtualenv venv ``

activate virtualenv

`` $ source venv/bin/activate ``

install packages within virtualenv 

`` $ pip install -r requirements.txt``

create migrations to sync with database

```$ python manage.py migrate```

create super admin

``$ python manage.py createsuperuser``

put username, email and password

``$ python manage.py runserver --settings=config.settings.dev``

go to the browser and check localhost:80000

to add blog first you need to login

localhost:8000/admin

provide username and password created earlier


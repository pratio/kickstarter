# Kickstarter stats
A Django app to show the stats of Kickstarter projects

###Running with Docker
After installing docker, go to the project directory 
and run `docker-compose up`. It will download the images of the
Django app and the postgres container.


###Running without Docker
Install the `requirements.txt`
Extract the `kickstarter.sql.7z` and load it into postgres.
Add the database details to the django settings file and run the 
django app using `./manage.py runserver` or with gunicorn 
`gunicorn kickstarter_django.wsgi:application --bind localhost:8001`


###Credits
>This couldn't have been easy without the datasets provided by 
https://webrobots.io/kickstarter-datasets/

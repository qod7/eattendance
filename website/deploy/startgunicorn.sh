#!/bin/bash

NAME="passion" # Name of the application
DJANGODIR=/home/passion/www/eattendance-web/website # Django project directory
BINDIP=127.0.0.1:3325 # bind gunicorn to this IP address
USER=passion # the user to run as
GROUP=passion # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=passion.settings.production # which settings file should Django use
DJANGO_WSGI_MODULE=passion.wsgi # WSGI module name

echo "Starting $NAME"

cd $DJANGODIR
# activate virtual environment
source /home/passion/.virtualenvs/passion/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/passion/.virtualenvs/passion/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=$BINDIP \
--log-file=-

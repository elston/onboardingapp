#!/bin/bash
PROJECT='onboardingapp'
PROJECTDIR='vagrant'
PORT=8000
if [[ $1 != '' ]]; then
    PORT=$1
fi
# ...
source /$PROJECTDIR/.env/$PROJECT/bin/activate
export DJANGO_SETTINGS_MODULE='settings.dev'
# ...
/$PROJECTDIR/$PROJECT/manage.py runserver 0.0.0.0:$PORT

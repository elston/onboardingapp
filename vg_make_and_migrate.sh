#!/bin/bash
set -e
PROJECT='onboardingapp'
PROJECTDIR='vagrant'

# ...
source /$PROJECTDIR/.env/$PROJECT/bin/activate
# ...
export DJANGO_SETTINGS_MODULE='settings.init'
# ...
/$PROJECTDIR/$PROJECT/manage.py makemigrations team
/$PROJECTDIR/$PROJECT/manage.py migrate
# ...

#!/bin/bash

PROJECT='onboardingapp'
PROJECTDIR='vagrant'
app=$1
if [[ ! $app ]]; then
    echo 'app not'
    exit 1
fi
name=$2
if [[ ! $name ]]; then
    echo 'name not'
    exit 1
fi
# ...
source /$PROJECTDIR/.env/$PROJECT/bin/activate
# ...
export DJANGO_SETTINGS_MODULE='settings.init'
 
# ...
/$PROJECTDIR/$PROJECT/manage.py loaddata ./$PROJECT/$app/fixtures/$name

#!/bin/bash
PROJECT='onboardingapp'
PROJECTDIR='vagrant'
# ..
if [[ $1 = '' ]]; then
    echo 'надо указать пользователя'
    exit 1
fi
# ....
source /$PROJECTDIR/.env/$PROJECT/bin/activate
export DJANGO_SETTINGS_MODULE='settings.dev'
# ...
/$PROJECTDIR/$PROJECT/manage.py changepassword $1
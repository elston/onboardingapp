#!/bin/bash
# ....
set -e

export PROJECT="onboardingapp"
export PROJDIR='vagrant'
export USER='vagrant'
export DJANGO_SETTINGS_MODULE='settings.init'
# ...
/$PROJDIR/bootstrap.sh
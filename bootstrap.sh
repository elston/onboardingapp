#!/bin/bash
# ....
set -e
# ...
if [[ ! $PROJECT ]]; then
    echo 'PROJECT not'
    exit 1
fi
if [[ ! $PROJDIR ]]; then
    echo 'PROJDIR not'
    exit 1
fi
if [[ ! $USER ]]; then
    echo 'USER not'
    exit 1
fi
if [[ ! $DJANGO_SETTINGS_MODULE ]]; then
    echo 'DJANGO_SETTINGS_MODULE not'
    exit 1
fi


#......................................


sudo apt-get update
sudo apt-get upgrade -y
#......................................

sudo apt-get -y install \
    python-dev \
    python3.4 \
    python3.4-dev \
    python-pip \
    python3-pip

sudo apt-get -y install \
    build-essential \
    libssl-dev \
    libffi-dev
#......................................
sudo pip install --upgrade \
    pip \
    virtualenv

sudo pip install \
    virtualenvwrapper

sudo pip install --upgrade \
    virtualenvwrapper

echo '....................Python Install OK'


#...
touch /home/$USER/.bashrc
echo " " >> /home/$USER/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/$USER/.bashrc

# ...mkvirtualenv
sudo -u $USER bash -c "
    mkdir -p /$PROJDIR/.env
    ln -s /$PROJDIR/.env /home/$USER/.virtualenvs
    export HOME=/home/$USER/
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv -p /usr/bin/python3 $PROJECT
"
# ...requirements
sudo -u $USER bash -c "
    export HOME=/home/$USER/
    source /$PROJDIR/.env/$PROJECT/bin/activate     
    pip install -r /$PROJDIR/requirements.txt    
"
#......................................

# .logs
LOGSDIR="/$PROJDIR/.logs/"
rm -rf $LOGSDIR
mkdir $LOGSDIR
echo '' > $LOGSDIR/django.log
echo '' > $LOGSDIR/nginx-access.log
echo '' > $LOGSDIR/nginx-error.log
echo '' > $LOGSDIR/gunicorn.log

# ..
sudo -u $USER bash -c "
    # ...
    export HOME=/home/$USER/
    source /$PROJDIR/.env/$PROJECT/bin/activate     
    # ..
    export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
    # ...
    # /$PROJDIR/$PROJECT/manage.py makemigrations team
    # /$PROJDIR/$PROJECT/manage.py makemigrations organization
    # /$PROJDIR/$PROJECT/manage.py makemigrations services    
    # /$PROJDIR/$PROJECT/manage.py migrate
    # /$PROJDIR/$PROJECT/manage.py loaddata /$PROJDIR/$PROJECT/team/fixtures/team_default_testdata.json
    # /$PROJDIR/$PROJECT/manage.py loaddata /$PROJDIR/$PROJECT/team/fixtures/org_default_testdata.json    
"

#...
sudo apt-get autoremove
sudo apt-get autoclean
echo 'YaHoo !!!'

exit 0
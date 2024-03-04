#!/bin/bash
djangoPID=`sudo lsof -t -i tcp:8000`
if [ -z "$djangoPID" ]
then
echo "No process is running"
else
sudo su -c "sudo kill -9 $djangoPID" -s /bin/sh devops_admin
fi

cd /home/devops_admin/project/nivish-api/nivish
git pull
find . -name *000*  -exec rm -rf {} \;
sudo pip3 install -r requirements.txt
python3 ./manage.py makemigrations
python3  ./manage.py migrate
sudo su -c "sudo python3 manage.py runserver 0.0.0.0:8000 >/dev/null 2>&1 < /dev/null &" -s /bin/sh devops_admin
sleep 21

djangoPID3=`sudo lsof -t -i tcp:8000`
if [ -z "$djangoPID3" ]
then
echo "Build was failed on Prod"
else
echo "Build was successful on Prod"
fi
exit

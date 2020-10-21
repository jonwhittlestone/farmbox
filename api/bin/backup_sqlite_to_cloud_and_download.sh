#!/bin/bash

echo "** This script should be run in {ROOT}/api/bin ** "

echo "This script performs the following:"
echo "  - Gets into the farmbox container"
echo "  - Removes the cloud backup"
echo "  - Backs up the sqlite file to the cloud"
echo "  - Uses the local Django management command to retrieve the backup to localhost"
echo ""
echo "** This script should be run in {ROOT}/api/bin ** "
echo ""
echo "=================================================================================="

CONTAINER_HOST_SSH_USER='jonwhittlestone'
CONTAINER_HOST_IP_ADDRESS='109.74.205.44'
export FARMBOX_DROPBOX_ACCESS_TOKEN=bSC8XiiZvuAAAAAAAAAADvNds2EgmP8TP058VpR1IvgotbBrlOgyYcXr8iWj7t71


ssh -tt jonwhittlestone@109.74.205.44 << 'ENDSSH'
docker exec "$(docker ps | grep farmbox_web | awk '{print $1}' | awk -F":" '{print $2}')" /bin/sh -c "python manage.py remove_remote_db";
exit
ENDSSH

ssh -tt jonwhittlestone@109.74.205.44 << 'ENDSSH'
docker exec "$(docker ps | grep farmbox_web | awk '{print $1}' | awk -F":" '{print $2}')" /bin/sh -c "python manage.py backup_db";
exit
ENDSSH

cd ../..
. venv/bin/activate
cd api
./manage.py restore_db

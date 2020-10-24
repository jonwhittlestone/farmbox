#!/bin/bash
# https://dev.to/coderasha/how-to-migrate-data-from-sqlite-to-postgresql-in-django-182h
echo "** This script should be run in {ROOT}/api/bin ** "

echo "This script copies a local sqlite db to a postgres destination db:"
echo "  - Dumps existing sqlite data to json"
echo "  - Resets/clears the cloud postgres table"
echo "  - Creates tables for apps without migrations (run-syncdb) on postgres destination"
echo "  - Deletes Contentype data using Django shell"
echo "  - Runs loadata to load the json data to the destination postgres"

echo ""
echo "** This script should be run in {ROOT}/api/bin ** "
echo ""
echo "=================================================================================="

DEST_ENVIRONMENT='staging'
DEST_APP='farmbox'
DEST_APP_ID="${DEST_APP}-${DEST_ENVIRONMENT}"


if [ -z ${DB_PASSWORD+x} ]; then
    echo ""
    echo "ERROR :( DB_PASSWORD for ${DEST_ENVIRONMENT} not set. Exiting."
    echo ""
    exit 0
fi

echo "* Dumping existing sqlite data to json .."
cd ../..
. venv/bin/activate
cd api
./manage.py migrate --settings farmbox.settings.sqlite
./manage.py dumpdata --settings farmbox.settings.sqlite > farmbox/sqlite_dump.json


echo "**********************************************************************************"
echo "* Resetting/clearing the cloud postgres table for app ${DEST_APP_ID}"
heroku pg:reset -a ${DEST_APP_ID} --confirm ${DEST_APP_ID}

echo "**********************************************************************************"
echo "  - Creating tables for apps without migrations (run-syncdb) on postgres destination"
./manage.py migrate --run-syncdb

echo "**********************************************************************************"
echo "TODO: Exclude contenttype data in django shell https://bit.ly/3dQHfup"

echo "**********************************************************************************"
echo "TODO: Load json data https://bit.ly/3dQHfup"

echo "**********************************************************************************"
echo "TODO: Compare table/record counts before and after"

#!/bin/sh

# ensure the database is up
sleep 5

# run database migrations
echo "<<<<<<<< Database Migrations Starts >>>>>>>>>"
flask db upgrade

sleep 5
echo "<<<<<<<< Database Migrations Completes >>>>>>>>>"

# Start the API with gunicorn
echo "<<<<<<<< Starting APP >>>>>>>>>"
flask run -h '0.0.0.0' -p 5000
# gunicorn -w 4 --bind=0.0.0.0:5000 manage:app --log-file=-

echo "<<<<<<<< APP Started on Port 5000 >>>>>>>>>"

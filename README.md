HOW TO INSTALL
==============

Create virtualenv and activate it

Install requirements  

	pip install -r requirements.txt

Change database settings accordingly

Create superuser  

	python manage.py createsuperuser  


Make migration  

	python manage.py migrate  


Generate ststic files and Start server  

	python manage.py collectstatic  
	python manage.py runserver

Load data into base_price table 


Underlying Logic
================
1- User uploads csv 

2- Read CSV and bulk insert data 

3- Trigger will take care of condition "If a rrp is below base_price , the status is approved else it moves to pending state"



Contact at +919599618855/dhirendra4work@gmail.com for any query
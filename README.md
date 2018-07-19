# Thumbnail Generator App
Thumbnail Generator Django App

## Update changes
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Create superuser
```bash
python3 manage.py createsuperuser
```
+ Enter name
+ Enter password

## Run server
```bash
python3 manage.py runserver
```

## Test thumbnail creation

### Create new _Content_ object
+ Goto
```
127.0.0.1:8000/admin
```
+ Login
+ Add content object
  * Select ``` Type ``` from the dropdown
  * Select ``` File ``` by clicking the _Browse_ button
  * Leave ``` Thumbnail ``` as empty
+ Click _Save_

### Check thumbnail file
+ Go to project main directory
+ Go to _media_ folder
+ New thumbnail could be found there with name as ``` (_orignal_file_name_).thm ```

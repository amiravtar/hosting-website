# Hosting website

A website for managing hosting written in **Django**

## How to run

#### Optional: Creating python virtual environment

```shell
python -m venv env
source env/bin/activate
```

### Install requirments

```shell
pip install -r requirements.txt
```

### Run migrations & Creat super user & Clear and creat log files

```shell
python manage.py migrate
python manage.py createsuperuser
./clear_log.sh
```

### Run django server

```shell
python manage.py runserver
```

and open http://localhost/admin in browser

# Kicksale
Welcome to Kicksale!
[Here](https://kicksale.herokuapp.com/) you are able to purchase on-demand sneakers for the lowest prices!

![Demo](https://user-images.githubusercontent.com/72108920/183554373-edaa5932-aef4-4eca-ad84-0257d324c128.gif)


Was developed using Python 3.9.6, Django 4.0.6 and Bootstrap 4.

# Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/elgizabbasov/kicksale.git
$ cd kicksale
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv myenv
$ source myenv/bin/activate
```

Then install the dependencies:

```sh
(myenv)$ pip install -r requirements.txt
```

Note the `(myenv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

### Perform Migrations

The SQLite3 database will not be shipped with the project and needs to be initialized before first run. To do this run:

```sh
(myenv)$ python manage.py makemigrations
```

to package up the initial models into individual migration files, and

```sh
(myenv)$ python manage.py migrate
```

directly after that. This will apply the initial models into the database. 

### Create a Superuser

To access the website's admin panel, you must also create a Django super user. This can be achieved by running:
```sh
(myenv)$ python manage.py createsuperuser
```

and following the instructions after. This is required for adding categories, products, and sizes.

```sh
(myenv)$ python manage.py runserver
```

And navigate to the host address presented in the terminal. (Often `http://127.0.0.1:8000/`).

# Models

# Views

# Templates

# Heroku
Kicksale is deployed using Heroku.
Heroku requires a `Procfile` and `runtime.txt` files to be present to deploy.
Application uses Heroku's PostgreSQL Free Plan as the database.
To have the server connecting to the correct DATABASE_URL, `dj-database-url` package is used which grabs the URL from the running dyno***

# Amazon S3
Application uses Amazon S3 Buckets to store static and media files inside Objects across the app.
To be able to integrate S3 with a Django app, several libraries are required:
`boto3`
`django-storages`


# Stripe Payment
All the payments are done through Stripe Elements; Kicksale does not collect any card information from users. 

![image](https://user-images.githubusercontent.com/72108920/179429046-dd680d32-010b-45de-994a-583ca04c7221.png)

# How to Contribute

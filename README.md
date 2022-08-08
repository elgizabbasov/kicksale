# Kicksale
Welcome to Kicksale!
Here you are able to purchase on-demand sneakers for the lowest prices!

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

Once `pip` has finished downloading the dependencies:

```sh
(myenv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

# Models

# Views

# Templates

# Heroku
Application uses Heroku's PostgreSQL as the database.

# Amazon S3
Application uses Amazon S3 buckets to store static and media files.

# Stripe Payment
All the payments are done through Stripe Elements; Kicksale does not collect any card information from users. 

![image](https://user-images.githubusercontent.com/72108920/179429046-dd680d32-010b-45de-994a-583ca04c7221.png)

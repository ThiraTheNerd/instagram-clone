# instagram-clone

An instagram clone built with django.

# Instagram Clone

#### Created on 12 July 2021

## author

https://github.com/ThiraTheNerd

---

## Access the website

Need the latest browser to be able to View

Follow this link https://igclone2020.herokuapp.com/

It is hosted by heroku

# Description

This is an instagram clone app. Instagram is the most popular photo sharing webapp. The app is not yet complete but will soon have all features ready that includes being able to post stories,reels and IGTV videos.

---

## User Stories

User Can :-

- Sign in to the application to start using.
- Upload my pictures to the application.
- See my profile with all my pictures.
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.

---

## Screenshots

###### Login Page

<img src="https://user-images.githubusercontent.com/51013354/125786038-154354b6-b6e4-4a62-9479-6e594ecbac10.png">

## Setup and Installation

To get the project .......

##### Clone Repository:

```bash
https://github.com/ThiraTheNerd/instagram-clone.git
```

##### Install and activate Virtual Enviroment envgallery

```bash
cd instagram-clone  && virtualenv virtual && source virtual/bin/activate
```

##### Install Dependencies

```bash
pip install -r requirements.txt
```

##### Setup Database

SetUp Database User,Password, Host then following Command

Create .env file

````bash
  SECRET_KEY='<SECRET_KEY>'
  DEBUG=True
  DB_NAME='database name'
  DB_USER='database user'
  DB_PASSWORD='password'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
  DISABLE_COLLECTSTATIC=1

 ```bash
python manage.py makemigrations instagram
````

Now Migrate

```bash
python manage.py migrate
```

##### Run Application

```bash
python3 manage.py server
```

##### Test Application

```bash
python manage.py test account
python manage.py test posts
```

Open the application on your browser `127.0.0.1:8000`.

### Access Django Admin

> > > Username: admin
> > > Password: admin2021

## Technology used

- HTML, CSS, Bootstrap

- Git

- Python3, Django Framework

- Heroku

## Bugs

- When you search for user that has multiple entries with the same name app crushes

## Contact Details

## thiragithinji@gmail.com

### License

This Project is under the [MIT](LICENSE) license

Copyright (c) 2021 ThiraTheNerd

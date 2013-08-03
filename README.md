Codez
=====
An online judge platform for algorithm competitions and training.

Requires:
---------
- [GNU Make](http://www.gnu.org/software/make/)
- [python 2.7.3](http://www.python.org/getit/)
- [django 1.4.2](https://www.djangoproject.com/download/)
- [django-registration](https://bitbucket.org/ubernostrum/django-registration/)
- [sqlite 3](http://www.sqlite.org/)
- Note: best way to install these is using pip:

```
sudo apt-get install pip
sudo pip install Django==1.4.5
sudo pip install django-registration
```

Instructions
------------
1. `make` builds the database and starts the dev server
2. go to [localhost:8000](http://localhost:8000/) and you should see the app running

### Other
1. `make run-mail` starts a dummy e-mail server (required only for account creation)
2. `make help` lists targets

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

Instructions
------------
1. `make` builds the database and starts the dev server
2. go to [localhost:8000](http://localhost:8000/) and you should see the app running

### Other
1. `make run-mail` starts a dummy e-mail server (required only for account creation)
2. `make help` lists targets

Sections
--------

1. Train
2. Solve
3. Compete
4. Propose
5. Host


TODO
---- 
1. Check out dom judge
2. Propose problem
3. Submit Solution
4. User Login
5. Create training course


FEATURES
--------
1. Upload Statement (simple markup, markdown->tex->html/pdf/ps )
2. Submit Solution
3. User accounts (can use Imperial accounts?)
4. Upload tutorial/course, linked with programming tasks
5. Virtual contest (e.g. for UTA programming challenges)
6. Social functions, achievements, progress tracking/motivation
7. Forum (separate thread)

IDEAS
-----
1. Guide progress (E.g. tutorial graph...)
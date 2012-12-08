all: db run

db: resetdb
	./manage.py loaddata judge/fixtures/initial_users.json
	./manage.py syncdb	

print-sql:
	./manage.py sql judge

syncdb:	
	./manage.py syncdb

resetdb:
	./manage.py reset judge
	./manage.py reset auth

run:
	./manage.py runserver

run-mail:
	python -m smtpd -n -c DebuggingServer localhost:1025

clean:
	find . -name "*.pyc" -exec $(RM) {} \;

dump:
	./manage.py dumpdata auth.User --indent 4 > judge/fixtures/initial_users.json
	./manage.py dumpdata judge --indent 4 > judge/fixtures/initial_data.json

help:
	@ echo "Available targets:"
	@ echo "  run-mail  -- start the e-mail server"
	@ echo "  run       -- start the django dev server"
	@ echo "  db        -- drop current database and re-populate from fixtures"
	@ echo "  syncdb    -- udpate database tables"
	@ echo "  syncdb    -- udpate database tables"
	@ echo "  print-sql -- print sql statements used to load the db"
	@ echo "  clean     -- remove .pyc files"

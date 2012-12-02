all: syncdb run

print-sql:
	python manage.py sql judge

syncdb:
	python manage.py syncdb

run:
	python manage.py runserver

run-mail:
	python -m smtpd -n -c DebuggingServer localhost:1025

clean:
	find . -name "*.pyc" -exec $(RM) {} \;

help:
	@ echo "Available targets:"
	@ echo "  run-mail   -- start the e-mail server"
	@ echo "  run        -- start the django dev server"
	@ echo "  syncdb     -- udpate database tables"
	@ echo "  print-sql  -- print sql statements used to load the db"
	@ echo "  clean      -- remove .pyc files"

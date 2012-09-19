python manage.py schemamigration feeds --auto
python manage.py schemamigration photos --auto
python manage.py schemamigration profiles --auto
python manage.py schemamigration photowalks --auto
python manage.py migrate feeds
python manage.py migrate photos
python manage.py migrate profiles
python manage.py migrate photowalks

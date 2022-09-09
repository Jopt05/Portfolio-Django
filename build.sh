set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

python manage.py migrate

python manage.py createsuperuser --username $DJANGO_SUPERUSER_USER --email $DJANGO_SUPERUSER_EMAIL --password $DJANGO_SUPERUSER_PASSWORD  --noinput
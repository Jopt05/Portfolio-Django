set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input --settings=jopt_portfolio.settings.prod
python manage.py migrate
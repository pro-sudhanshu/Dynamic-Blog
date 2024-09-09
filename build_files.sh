echo "BUILD START"
python3.9 -m pip install -r requirements.txt
echo "BUILD END"

echo "MAKE MIGRATIONS"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
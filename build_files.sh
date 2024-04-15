# pip install -r requirements.txt 
# python3.9 manage.py collectstatic

#!/bin/bash

echo "Pip installation/updation and virtual environment activation. . ."
python3.9 -m ensurepip
python3.9 -m pip install --upgrade pip
python3.9 -m venv myenv
source myenv/bin/activate

echo "Installing requirements.txt. . ."
python3.9 -m pip install -r requirements.txt

echo "Making migrations. . ."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect static. . ."
python3.9 manage.py collectstatic --noinput


# pip install -r requirements.txt 
# python3.9 manage.py collectstatic

#!/bin/bash
python3.9 -m ensurepip
python3.9 -m pip install --upgrade pip
python3.9 -m venv myenv
source myenv/bin/activate
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput


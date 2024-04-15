# pip install -r requirements.txt 
# python3.9 manage.py collectstatic

#!/bin/bash
python3.8 -m ensurepip
python3.8 -m pip install --upgrade pip
python3.8 -m venv myenv
source myenv/bin/activate
python3.8 -m pip install -r requirements.txt
python3.8 manage.py collectstatic --noinput


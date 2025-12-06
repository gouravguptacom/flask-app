# flask-app

```
python -m venv .venv
source .venv/bin/activate
pip freeze
pip install -r requirements.txt
pip freeze
touch app.py
python -m flask run -> this will run the app in default port, even if you specify the port
python app.py -> this will run the app with port you specified
```

### create requirements.txt

```
pip install flask
python freeze > requirements.txt
pip install -r requirements.txt
```
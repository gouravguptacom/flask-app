from flask import request, render_template, redirect, url_for, Blueprint

from blueprintapp.app import db
from blueprintapp.blueprints.peoples.models import People

peoples = Blueprint('peoples', __name__, template_folder="templates")

@peoples.route("/")
def index():
    peoples = People.query.all()
    return render_template("peoples/index.html", peoples=peoples)

@peoples.route("/create", methods=["GET", "POST"])
def create():
    if request.method == 'GET':
        return render_template("peoples/create.html")
    elif request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        job = request.form.get('job')

        job = job if job != '' else None

        people = People(name=name, age=age, job=job)

        db.session.add(people)
        db.session.commit()

        return redirect(url_for('peoples.index'))
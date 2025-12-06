from flask import render_template, Blueprint

cores = Blueprint('cores', __name__, template_folder="templates")

@cores.route("/")
def index():
    return render_template("cores/index.html")

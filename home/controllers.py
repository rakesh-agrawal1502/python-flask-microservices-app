from flask import render_template, Blueprint

home = Blueprint('home', __name__)


@home.route("/", methods=['GET'])
def land():
    return render_template("landing.html")


@home.route("/home", methods=['GET'])
def homepage():
    # return "<h1>Hello World</h1>"
    return render_template("home.html")


@home.route("/home/about", methods=['GET'])
def about():
    return render_template("about.html")

from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main_blueprint.route("/webcam", methods=["GET"])
def webcam():
    return render_template("webcam.html")
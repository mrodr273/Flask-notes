from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesytem"
Session(app)

# @app.route('/set/')
# def set():
#     session['key'] = 'value'
#     return 'ok'

# @app.route('/get/')
# def get():
#     return session.get('key', 'not set')

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index.html", notes=notes)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if session.get("notes") is None:
#         session["notes"] = []
#     if request.method == "POST":
#         note = request.form.get("note")
#         session["notes"].append(note)
#     return render_template("index.html", notes=session["notes"])
import database
import flask
from _init_ import app
from user_auth.register import newUser


@app.route("/users/login", methods = ["GET", "POST"])
def login():
    if flask.request.method == "POST":
        flask.session["user"] = newUser
        pass
    else:
        context = {}
        flask.render_template("/users/login", **context)
    pass

def login_handler():
    pass
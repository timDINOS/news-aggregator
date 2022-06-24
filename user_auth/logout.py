import database
import flask
from _init_ import app


@app.route("/users/logout", methods=["POST"])
def logout():
    if flask.request.method == "POST":
        flask.session.clear()
        flask.redirect("/users/login")
    else:
        context = {}
        return flask.render_template("/users/logout", **context)



import database
import flask
from _init_ import app
import json

@app.route("/users/register", methods=["GET", "POST"])
def register():
    new_user = {}
    if flask.request.method == "POST":
        typed_name = flask.request.form['name']
        if not typed_name:
            flask.abort(400)
        new_user["name"] = typed_name
        typed_email = flask.request.form['email']
        if not typed_email:
            flask.abort(400)
        new_user["email"] = typed_name
        typed_user = add_username()
        new_user["username"] = typed_user
        typed_pass = add_password()
        new_user["password"] = typed_pass
        new_user_json = json.dumps(new_user)
        insert_into_db(new_user_json)
        flask.session['username'] = typed_user
    else:
        context = {}
        flask.render_template("/users/register.html", **context)


def add_username():
    user_name1 = flask.request.form['username']
    retyped_user = flask.request.form['retype_username']
    if user_name1 != retyped_user:
        flask.abort(400)
    if user_name1 is None or retyped_user is None or len(user_name1) > 30 or database.collection_user_profile.find_one({"username": user_name1}) is not None:
        flask.abort(400)
    return user_name1


def add_password():
    pass



def insert_into_db(new_user):
    database.collection_user_profile.insert_one(new_user)
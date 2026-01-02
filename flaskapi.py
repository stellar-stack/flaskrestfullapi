from flask import Flask,request, url_for
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello world </p>"

@app.route("/hello/")
def hello():
    name = request.args.get("name", "Furqan")
    return f'hello, {name}'

# @app.route("/user/<username>")
# def show_user_profile(username):
#     return f"{username}\'s profile"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"post number: {post_id}"

@app.route("/subpath/<path:subpath>")
def r_subpath(subpath):
    return f"path: {escape(subpath)}"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    # print(url_for("hello_world"))
    # print(url_for('hello', next="/", name = "rum"))
    # print(url_for("show_user_profile", username="Romeo"))
    # print(url_for('show_post', post_id="1"))
    # print(url_for('r_subpath', subpath="File structure"))
    print(url_for('profile', username='John Doe'))

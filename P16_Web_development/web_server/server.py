from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<username>')
def hello_world(username=None):
    return render_template('index.html',name=username)


@app.route('/<username>/<int:post_id>')
def show_post(username=None,post_id=None):
    return render_template('index.html',name=username,post_id = post_id)


@app.route("/blog")
def blog():
    return "<p> this is blog page </p>"


@app.route("/about")
def about():
    return render_template('about.html')



from flask import Blueprint, redirect, request, render_template, url_for


entering = Blueprint("entering", __name__)


@entering.route("/signin")
def signin():
    return "Sign In"


@entering.route("/signup")
def signup():
    return "Sign Up"


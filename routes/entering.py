from flask import Blueprint, redirect, request, render_template, url_for
from database.user import USERS


entering = Blueprint("entering", __name__)


@entering.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        try:
            error = request.args.get("error")
            if error:
               return render_template("signin.html", error=error) 
        except:
            ...
        
        return render_template("signin.html")

    user = request.json

    for client in USERS:
        if user["email"] == client["email"] and \
           user["password"] == client["password"]:
            return redirect(url_for("entering.signup"))     
            
    return redirect(url_for("entering.signin", error=True))


@entering.route("/certo")
def certo(): 
    return "<p>Tudo certo</p>"


@entering.route("/errado")
def errado():
    return "<p>Senha e/ou email errado</p>"


@entering.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


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
            return render_template("final_page.html")
 
    return redirect(url_for("entering.signin", error=True))


@entering.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
       return render_template("signup.html")

    user = request.json
    name = user["name"]
    email = user["email"]
    password = user["password"]
    cpassword = user["cpassword"]

    if password != cpassword:
        return render_template("signup.html", error=True)

    if not name or not email or not password or not cpassword:
        return render_template("signup.html", error=True)


    new_user = {"id": len(USERS) + 1, "name": name, "email": email, "password": password}
    USERS.append(new_user)

    return render_template("final_page.html")


# Será removido posteriormente
@entering.route("/list_users")
def list_users():
    return render_template("list_users.html", users=USERS)


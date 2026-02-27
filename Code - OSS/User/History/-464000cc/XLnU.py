import os
from dotenv import load_dotenv

load_dotenv()


from flask import Flask, render_template, request, redirect, session
import firebase
from firestore import get_user_by_email, create_user
from auth import hash_password, verify_password, login_required, admin_required
from datetime import datetime

app = Flask(__name__)
app.secret_key = "asd2"  # use env var on Cloud Run

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        doc = get_user_by_email(email)
        if not doc:
            return "Invalid credentials", 401

        user = doc.to_dict()
        if not verify_password(user["password_hash"], password):
            return "Invalid credentials", 401

        session["user"] = email
        session["role"] = user["role"]
        session["tenant_id"] = user["tenant_id"]

        return redirect("/dashboard")

    return render_template("login.html")



@app.route("/admin/users/create", methods=["GET", "POST"])
@login_required
@admin_required
def admin_create_user():
    if request.method == "POST":
        create_user({
            "email": request.form["email"],
            "password_hash": hash_password(request.form["password"]),
            "role": request.form["role"],
            "tenant_id": request.form["tenant_id"],
            "created_at": datetime.utcnow()
        })
        return redirect("/dashboard")

    return render_template("admin_create_user.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html",
        email=session.get("user"),
        role=session.get("role"),
        tenant_id=session.get("tenant_id"),
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)


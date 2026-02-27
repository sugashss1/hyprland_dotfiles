from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, redirect, url_for
from functools import wraps

def hash_password(password):
    return generate_password_hash(password)

def verify_password(hash, password):
    return check_password_hash(hash, password)

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("role") != "admin":
            return "Forbidden", 403
        return f(*args, **kwargs)
    return wrapper

def manager_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("role") != "manager" and session.get("role") != "admin":
            return "Forbidden", 403
        return f(*args, **kwargs)
    return wrapper


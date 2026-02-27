from google.cloud import firestore

db = firestore.Client()

def get_user_by_email(email):
    users = db.collection("users").where("email", "==", email).limit(1).stream()
    return next(users, None)

def create_user(data):
    db.collection("users").add(data)

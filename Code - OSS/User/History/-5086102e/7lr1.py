import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv

load_dotenv()

if not firebase_admin._apps:
    cred = credentials.Certificate("multi-tanant-firebase.json")
    firebase_admin.initialize_app(cred)
else:
    import firebase_admin
    firebase_admin.initialize_app()


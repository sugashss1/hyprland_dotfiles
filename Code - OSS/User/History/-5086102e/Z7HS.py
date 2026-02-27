import os
import firebase_admin
from firebase_admin import credentials

if not firebase_admin._apps:
    if os.getenv("K_SERVICE"):  # Running on Cloud Run
        firebase_admin.initialize_app()
    else:  # Local development
        cred = credentials.Certificate("multi-tanant-firebase.json")
        firebase_admin.initialize_app(cred)

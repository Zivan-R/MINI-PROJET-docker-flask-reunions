from app import app
from models import db
import time

with app.app_context():
    retries = 5
    for i in range(retries):
        try:
            db.create_all()
            print("Database initialisée correctement")
            break
        except Exception as e:
            print(f"Essai {i+1} échoué. Nouvel essai dans 5 secondes...")
            time.sleep(5)

    else:
        print("Impossible d'initialiser la database...")

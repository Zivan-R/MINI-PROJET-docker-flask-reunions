import time
from sqlalchemy import create_engine
import os

db_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
retries = 5
engine = create_engine(db_uri)

for i in range(retries):
    try:
        engine.connect()
        print("Database is ready!")
        exit(0)
    except Exception as e:
        print(f"Waiting for db... {e}")
        time.sleep(5)

print("Database not ready, exiting")
exit(1)

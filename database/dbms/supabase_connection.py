from contextlib import contextmanager
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv(override=True)


@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            dbname=os.getenv("DBNAME")
        )
        print("Connection successful!")
        yield connection

    except Exception as e:
        print(f"Failed to connect: {e}")
        if connection:
            connection.rollback()
        raise
    finally:
        if connection is not None:
            connection.close()
            print("Connection closed.")

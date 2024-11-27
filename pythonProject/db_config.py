import os
import mysql.connector
from dotenv import load_dotenv

#
load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),  # Database host
        port=os.getenv('DB_PORT'),  # Database port
        user=os.getenv('DB_USER'),  # Database username
        password=os.getenv('DB_PASSWORD'),  # Database password
        database=os.getenv('DB_NAME'),  # Database name
    )


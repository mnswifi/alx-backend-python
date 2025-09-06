#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import csv
import uuid

# Initial connection parameters
host = "172.17.0.2"
user = "root"
password = "admin@alx"
database = "ALX_prodev"

def connect_db():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
    
def create_database(connection):
    """Create ALX_prodev database if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None

def create_table(connection):
    """Create user_data table if not exists."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX (user_id)
            );
        """)
        connection.commit()
        print("Table user_data created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

def insert_data(connection, csv_file):
    """Insert data from CSV file into user_data table."""
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']

                # Check if record already exists
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                if cursor.fetchone():
                    print(f"Record with email {email} already exists. Skipping insertion.")
                    continue

                # Insert data into user_data table
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s);
                """, (user_id, name, email, age))
        connection.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error inserting data: {e}")

def stream_rows(connection, query="SELECT * FROM user_data;"):
    """Generator to stream rows from user_data table."""
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            yield row
        cursor.close()
    except Error as e:
        print(f"Error streaming rows: {e}")

   
#!/usr/bin/python

import seed  # reuse seed.py connection logic

def stream_users():
    """
    Generator that streams rows from user_data table one by one.
    """
    connection = seed.connect_to_prodev()
    if not connection:
        print("Could not connect to ALX_prodev")
        return

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")

    for row in cursor:   # <-- only one loop
        yield row

    cursor.close()
    connection.close()

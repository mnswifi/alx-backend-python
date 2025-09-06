#!/usr/bin/python3

import seed # resuse connection functions

def stream_users_in_batches(batch_size):
    """
    Generator function that yields users in batches of a specified size.
    """
    connection = seed.connect_to_prodev()
    if not connection:
        print("Could not connect to ALX_prodev")
        return
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    # Yield any remaining users in the last batch
    if batch:
        yield batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """
    Processes users over age 25 in batches and prints them.
    """
    for batch in stream_users_in_batches(batch_size):
        batch = [user for user in batch if int(user[3]) > 25]
        for user in batch:
            user_dict = {
                "user_id": str(user[0]),
                "name": user[1],
                "email": user[2],
                "age": int(user[3])
            }
            print(user_dict, end="\n")



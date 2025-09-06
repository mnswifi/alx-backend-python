#!/usr/bin/python3

import seed  # reuse seed.py connection logic

def stream_user_ages():
    """
    Generator that streams ages from user_data table one by one.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data;")
    
    for (age,) in cursor:
        yield int(age)
        
    cursor.close()
    connection.close()
    
def calculate_average_age():
    """
    Calculates and returns the average age of users.
    """
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
        
    if count == 0:
        return 0
    
    return total_age / count
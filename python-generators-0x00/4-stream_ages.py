#!/usr/bin/env python3

from seed import connect_to_prodev

def stream_user_ages():
    """Generator that yields user ages one by one from the database"""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT age FROM user_data")
    while True:
        row = cursor.fetchone()
        if not row:
            break
        yield row['age']

def calculate_average_age():
    """
    Calculates and prints the average age of users without loading the
    entire dataset into memory.
    """
    total = 0
    count = 0
    for age in stream_user_ages():
        total += int(age)
        count += 1

    if count != 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")


if __name__ == "__main__":
    calculate_average_age()



# ["def paginate_users", "SELECT * FROM user_data LIMIT", "OFFSET"]
# ["yield", "return"]
# ["FROM user_data", "SELECT", "+"]

#!/usr/bin/python3
# seed = __import__('seed')
from seed import connect_to_prodev


def paginate_users(page_size, offset):
    """Fetch a paginate users"""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """Lazily fetch of users from the database"""
    offset = 0
    while True:
        page = paginate_users(page_size,0)
        if not page:
            break
        yield page
        offset += page_size


# SELECT FROM LIMIT WHERE
# ["def paginate_users", "SELECT * FROM user_data LIMIT", "OFFSET"]
# ["paginate_users(page_size, offset)"]

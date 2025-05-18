#!/usr/bin/env python3

from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """
        Generator that yields users in batch
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """
        Processing each batch to print users who are over age 25
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = [user for user in batch if user[3] > 25]
        if filtered_batch:
            print(filtered_batch, "\n")



# ["FROM user_data", "SELECT"]
# ["25", ">"]
# ["yield", "return"]

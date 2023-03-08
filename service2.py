import psycopg2
import time
import random
from transaction import Transaction
from credentials import conn
from sql_queries import create_table, update_transactions
create_table(conn)
if __name__ == "__main__":
    while True:
        update_transactions(conn)

        print("updated")
        time.sleep(20)

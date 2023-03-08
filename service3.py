import psycopg2
import time
from transaction import Transaction
from credentials import conn
from sql_queries import create_table, lol_transactions
create_table(conn)
if __name__ == "__main__":
    while True:
        lol_transactions(conn)

        print("done")
        time.sleep(20)
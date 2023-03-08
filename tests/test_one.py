from sqlalchemy import create_engine
from transaction import Transaction
from sql_queries import insert_transaction, lol_transactions, get_transactions, update_transactions


def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    transaction = Transaction(
        description="test_description",
        price=100,
        quantity=1000,
        amount=0,
    )
    insert_transaction(conn, transaction)

    transactions = get_transactions(conn)
    assert len(transactions) == 4
    transaction = transactions[-1]
    assert transaction.description == "test_description"

    update_transactions(conn)
    transactions = get_transactions(conn)
    for transaction in transactions:
        assert transaction.price * transaction.quantity == transaction.amount
        assert transaction.status == "calculated"

    lol_transactions(conn)
    transactions = get_transactions(conn)
    for transaction in transactions:
        if transaction.status == 'wow':
            assert transaction.amount>999

            


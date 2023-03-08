from dataclasses import dataclass

@dataclass

class Transaction:
    description: str
    price: int
    quantity: int
    amount: int
    created: str = ""
    status: str = "new"
    id: int = None
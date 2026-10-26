from src.services import net_balance, simplify_debts


def test_single_expense_equal_split():
    """
    Caso 1: Un único gasto dividido a partes iguales.
    Alice paga 90€ entre Alice, Bob y Charlie (30€ cada uno).
    """
    transactions = [
        {"payer": "Alice", "amount": 90.0, "between": ["Alice", "Bob", "Charlie"]}
    ]

    balances = net_balance(transactions)

    # Alice puso 90 y gastó 30 -> saldo +60
    assert balances["Alice"] == 60.0
    # Bob y Charlie no pusieron nada y gastaron 30 -> saldo -30 cada uno
    assert balances["Bob"] == -30.0
    assert balances["Charlie"] == -30.0

    # Probamos las transferencias
    transfers = simplify_debts(balances)

    assert len(transfers) == 2
    assert {"from": "Bob", "to": "Alice", "amount": 30.0} in transfers
    assert {"from": "Charlie", "to": "Alice", "amount": 30.0} in transfers


def test_circular_debt_simplification():
    """
    Caso 2: Deuda circular.
    Alice debe cobrar 20€, Bob queda a 0€, y Charlie debe 20€.
    El algoritmo debe resolverlo con una sola transferencia directa.
    """
    balances = {"Alice": 20.0, "Bob": 0.0, "Charlie": -20.0}

    transfers = simplify_debts(balances)

    assert len(transfers) == 1
    assert transfers[0] == {"from": "Charlie", "to": "Alice", "amount": 20.0}


def test_everyone_even():
    """
    Caso 3: Todos están a cero.
    No debería generarse ninguna transferencia.
    """
    balances = {"Alice": 0.0, "Bob": 0.0}

    transfers = simplify_debts(balances)

    assert len(transfers) == 0
    

    
# Probar tests: uv run python -m pytest
# Probar solo estos tests: uv run python -m pytest tests/test_settlement.py
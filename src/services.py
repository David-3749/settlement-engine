def net_balance(transactions: list[dict]) -> dict[str, float]:
    balances: dict[str, float] = {}

    for t in transactions:
        payer = t["payer"].strip()
        amount = t["amount"]
        between = [p.strip() for p in t["between"]]

        if amount <= 0 or not between:
            continue

        balances[payer] = balances.get(payer, 0.0) + amount

        split_amount = amount / len(between)

        for person in between:
            balances[person] = balances.get(person, 0.0) - split_amount

    return {k: round(v, 2) for k, v in balances.items() if abs(v) > 0.01}


def simplify_debts(balances: dict[str, float]) -> list[dict]:
    settlements = []

    creditors = [[person, amount] for person, amount in balances.items() if amount > 0.01]
    debtors = [[person, -amount] for person, amount in balances.items() if amount < -0.01]

    creditors.sort(key=lambda x: x[1], reverse=True)
    debtors.sort(key=lambda x: x[1], reverse=True)

    i = 0
    j = 0

    while i < len(creditors) and j < len(debtors):
        creditor_name, credit = creditors[i]
        debtor_name, debt = debtors[j]

        settled_amount = min(credit, debt)
        settled_amount = round(settled_amount, 2)

        creditors[i][1] -= settled_amount
        debtors[j][1] -= settled_amount

        if settled_amount > 0:
            settlements.append(
                {
                    "from": debtor_name,
                    "to": creditor_name,
                    "amount": settled_amount,
                }
            )
        if creditors[i][1] < 0.01:
            i += 1
        if debtors[j][1] < 0.01:
            j += 1

    return settlements


lista = [
    {"payer":"David","amount":60.0,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]},
    {"payer":"Hugo","amount":92.5,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]},
    {"payer":"Mate","amount":81.0,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]},
    {"payer":"Mate","amount":76.0,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]},
    {"payer":"Miguel","amount":44.6,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]},
    {"payer":"Hugo","amount":86.4,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]},
    {"payer":"Samu","amount":120.3,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]},
    {"payer":"David","amount":80.7,"between":["Hugo", "Miguel", "David", "Mate", "Samu"]}
]

saldos_netos = net_balance(lista)
print(saldos_netos)

plan = simplify_debts(saldos_netos)
print(plan)

for transfer in plan:
    print(f"{transfer['from']} paga a {transfer['to']} {transfer['amount']} €")

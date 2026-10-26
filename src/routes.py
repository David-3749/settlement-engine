from fastapi import APIRouter, HTTPException

from src.schemas import SettleRequest
from src.services import net_balance, simplify_debts

router = APIRouter()


@router.get("/")
def health_check():
    return {"status": "ok", "service": "Settlement Engine API"}


@router.post("/settle")
def settle_expenses(request: SettleRequest):
    if not request.transactions:
        raise HTTPException(status_code=400, detail="Debes enviar al menos una transacción.")

    raw_txs = [t.model_dump() for t in request.transactions]

    net = net_balance(raw_txs)
    plan = simplify_debts(net)
    
    
    for transfer in plan:
        print(f"{transfer['from']} paga a {transfer['to']} {transfer['amount']} €")

    return {
        "net_balances": net,
        "settlements": plan,
        "total_transfers": len(plan),
    }
    
    
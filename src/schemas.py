from pydantic import BaseModel, Field



class TransactionItem(BaseModel):
    payer: str = Field(..., min_length=1, example="David")
    amount: float = Field(..., gt=0, example= 60.0)
    between: list[str] = Field(..., min_length=1, example=["Hugo", "Ossa", "David"])


class SettleRequest(BaseModel):
    transactions: list[TransactionItem]
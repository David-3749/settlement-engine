from fastapi import FastAPI
from src.routes import router

app = FastAPI(
    title="Expense Settlement Engine",
    description="API para calcular saldos y simplificar deudas entre amigos.",
    version="1.0.0",
)

# Conectamos las rutas definidas en routes.py
app.include_router(router)

# Para iniciar: uv run uvicorn main:app --reload
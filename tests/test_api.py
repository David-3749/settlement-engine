from fastapi.testclient import TestClient
from main import app

# Creamos un cliente simulado que hace peticiones directamente a tu app
client = TestClient(app)


def test_health_check():
    """Comprueba que el endpoint raíz responda 200 OK."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "Settlement Engine API"}


def test_settle_endpoint_success():
    """Comprueba que una petición válida a /settle devuelva el resultado esperado."""
    payload = {
        "transactions": [
            {
                "payer": "David",
                "amount": 90.0,
                "between": ["David", "Hugo", "Ossa"]
            }
        ]
    }

    response = client.post("/settle", json=payload)

    assert response.status_code == 200
    data = response.json()

    # Verificamos los saldos y transferencias devueltos
    assert data["net_balances"]["David"] == 60.0
    assert data["net_balances"]["Hugo"] == -30.0
    assert data["net_balances"]["Ossa"] == -30.0
    assert data["total_transfers"] == 2


def test_settle_endpoint_validation_error():
    """Comprueba que Pydantic bloquee importes inválidos con error 422."""
    bad_payload = {
        "transactions": [
            {
                "payer": "David",
                "amount": -50.0,  # Importe inválido (gt=0)
                "between": ["Hugo"]
            }
        ]
    }

    response = client.post("/settle", json=bad_payload)
    assert response.status_code == 422
    
# Probar tests: uv run python -m pytest
# Probar solo estso tests: uv run python -m pytest tests/test_api.py
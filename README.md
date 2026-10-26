# 💸 Expense Settlement Engine API

[![CI Pipeline](https://github.com/David-3749/settlement-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/David-3749/settlement-engine/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![uv](https://img.shields.io/badge/managed%20by-uv-DE5FE9?logo=astral)

Motor de cálculo y API REST de alto rendimiento para la simplificación óptima de deudas compartidas (estilo Splitwise). Implementa un algoritmo voraz de dos punteros sobre balances netos para reducir el volumen de transacciones bancarias requeridas.

---

## 🚀 Características

- **Algoritmo de liquidación voraz:** Reducción de grafos de deudas mediante consolidación de saldo neto y emparejamiento con dos punteros ($O(n \log n)$).
- **API REST con FastAPI:** Endpoints tipados y validados con **Pydantic V2**.
- **Gestión moderna con `uv`:** Tiempos de resolución e instalación de dependencias ultrarrápidos.
- **Entorno aislado con Docker:** Contenedor optimizado basado en `python:3.11-slim-bookworm`.
- **Integración Continua (CI):** Flujo de trabajo automatizado con **GitHub Actions** y suite completa de pruebas en **pytest**.

---

## 🛠️ Requisitos Previos

- [uv](https://docs.astral.sh/uv/) (recomendado) o Python 3.11+
- [Docker](https://www.docker.com/) (opcional, para despliegue en contenedor)

---

## 💻 Instalación y Desarrollo Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/David-3749/settlement-engine.git](https://github.com/David-3749/settlement-engine.git)
   cd settlement-engine
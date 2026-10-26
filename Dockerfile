# 1. Usamos una imagen ligera oficial de Python
FROM python:3.11-slim-bookworm

# 2. Instalamos uv copiando el binario desde su imagen oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Habilitamos la compilación de bytecode para acelerar el arranque
ENV UV_COMPILE_BYTECODE=1

# 5. Copiamos solo los archivos de dependencias primero (aprovecha la caché de Docker)
COPY pyproject.toml uv.lock ./

# 6. Instalamos únicamente las dependencias de producción (sin herramientas de test)
RUN uv sync --frozen --no-install-project --no-dev

# 7. Copiamos el código fuente de la aplicación
COPY src/ ./src/
COPY main.py ./

# 8. Añadimos el entorno virtual generado por uv al PATH del sistema
ENV PATH="/app/.venv/bin:$PATH"

# 9. Exponemos el puerto estándar donde escuchará la API
EXPOSE 8000

# 10. Comando de arranque con Uvicorn escuchando en todas las interfaces de red
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
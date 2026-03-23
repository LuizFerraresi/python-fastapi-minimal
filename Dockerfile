FROM python:3.13.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /company

# Create a dedicated group and user (non-root)
RUN groupadd appgroup && \
    useradd -G appgroup appuser && \
    chown -R appuser:appgroup /company

COPY --chown=appuser:appgroup requirements/runtime.txt requirements.txt

# Upgrade package manager and install requirements
RUN pip install --requirement requirements.txt \
    --upgrade pip build wheel setuptools \
    --no-cache-dir

COPY --chown=appuser:appgroup app/ app/

USER appuser

EXPOSE 8000

CMD [ "uvicorn", "app.api:app" ]

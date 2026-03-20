FROM python:3.13.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /company

COPY requirements.txt .

RUN pip install --requirement requirements.txt \
    --upgrade pip build wheel setuptools \
    --no-cache-dir

COPY app/ app/

EXPOSE 8000

CMD [ "uvicorn", "app.api:app" ]

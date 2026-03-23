
# Minimal Python Application with FastAPI

## Requirements

- [ ] Python >= 3.13
- [ ] Docker
- [ ] direnv

## Setup

### Upgrade PIP and Wheels

```bash
pip install --upgrade pip build wheel setuptools virtualenv
```

### Install

```bash
# create virtual environment
python -m virtualenv .venv

# activate virtual environment - Linux
source .venv/bin/activate

# install requirements
pip install --requirement requirements/development.txt

# export environment variables
direnv allow .
```

## Running

> [!TIP]
> Check the [FastAPI Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/) and
> [Uvicorn Deployment](https://uvicorn.dev/deployment/) documentation.

### FastAPI CLI

```bash
# development 
fastapi dev app/api.py --reload

# production mode
fastapi run app/api.py
```

### uvicorn

```bash
uvicorn app.api:app
```

### Docker

```bash
# build image
docker buildx build . --tag fastapi-minimal:latest

# run container
docker run --publish 8000:8000 --env-file .env.sample fastapi-minimal:latest
```

## Making Requests

URL: http://localhost:8000

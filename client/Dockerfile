FROM python:3.12

WORKDIR /app

COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ../.env .
COPY ../client ./client
COPY ../config.py ./client

CMD python3 client/main.py

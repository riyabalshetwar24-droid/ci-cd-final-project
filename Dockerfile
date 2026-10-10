FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY tests ./tests
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]

FROM python:3.13-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

RUN useradd -r -u 10001 bot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R bot:bot /app

USER bot

CMD ["python", "-u", "-m", "app.main"]

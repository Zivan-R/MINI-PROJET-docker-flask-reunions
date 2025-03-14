FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential default-libmysqlclient-dev

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]

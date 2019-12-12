FROM python:3.7-slim

RUN apt-get update

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app

ENV FLASK_APP /app/app.py
ENV FLASK_DEBUG 1

CMD ["flask" , "run", "-h", "0.0.0.0", "-p", "8080"]

FROM python:3.12.3-slim

WORKDIR /scripts/

ADD requirements.txt .

RUN pip3 install -r requirements.txt

ADD main.py main.py
ADD logic/* logic/
ADD models/* models/

EXPOSE 3000

ENTRYPOINT ["gunicorn" , "-b", "0.0.0.0:3000", "main:app"]

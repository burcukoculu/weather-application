FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python temperature_app.py
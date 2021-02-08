FROM python:3.8-slim-buster

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY . /app/gubble
WORKDIR /app/gubble

CMD [ "python", "./main.py" ]

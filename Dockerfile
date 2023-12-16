FROM python:3.9-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt
    
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
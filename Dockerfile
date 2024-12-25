FROM python:3.11-slim

WORKDIR /bot 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

COPY . . 
COPY .env.docker .env

CMD python main.py
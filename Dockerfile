FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt 

COPY . .

RUN pytest

EXPOSE 5000

ENV FLASK_APP=run.py DATABASE_URL=postgresql://postgres:postgres@benford_db:5432/postgres

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
FROM python:3.9-slim

RUN pip install django

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

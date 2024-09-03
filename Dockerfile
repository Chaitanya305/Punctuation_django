FROM django

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "manage.py", "runserver" "0.0.0.0:8000" ]
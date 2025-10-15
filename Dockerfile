FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt ./app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py"]

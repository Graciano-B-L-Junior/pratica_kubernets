FROM python:3.10.14-bullseye

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD [ "python", "app.py" ]
FROM python:3.9.18-slim-bullseye
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD [ "python", "app.py" ]
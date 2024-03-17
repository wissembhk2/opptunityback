FROM python:3.9.15-slim-buster

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
#COPY ./.env .env
ENV PYTHONPATH=/app

CMD ["gunicorn", "app.main:app",  "--worker-class","uvicorn.workers.UvicornWorker","-b","0.0.0.0:8001"]

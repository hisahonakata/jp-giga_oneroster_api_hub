FROM tiangolo/uvicorn-gunicorn:python3.11

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"
RUN apt-get update && apt-get install -y libsqlite3-dev

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
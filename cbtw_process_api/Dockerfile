FROM python:3.11

WORKDIR /server-docker
ENV ENV=workspace/aircrafts 

RUN python3 -m venv /${ENV}

COPY ./server /server-docker/
COPY ./requirements.txt /server-docker/requirements.txt

RUN /${ENV}/bin/python3 -m pip install --upgrade pip
RUN /${ENV}/bin/pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5000

CMD ../${ENV}/bin/uvicorn main:app --reload \
    --port 5000 --host 0.0.0.0
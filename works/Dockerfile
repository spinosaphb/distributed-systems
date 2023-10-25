FROM alpine:3.7

RUN apk add --no-cache python3-dev bash \
    && pip3 install --upgrade pip


WORKDIR /distributed-systems

COPY . /distributed-systems

RUN chmod +x /distributed-systems/run.sh

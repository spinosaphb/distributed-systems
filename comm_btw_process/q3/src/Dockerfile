FROM alpine:3.11

RUN apk add --no-cache python3-dev bash \
    && pip3 install --upgrade pip


WORKDIR /src

COPY . /src

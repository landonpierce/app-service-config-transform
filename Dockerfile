FROM python:3.10.4-alpine3.15

WORKDIR /src

ENTRYPOINT [ "python", "main.py" ]

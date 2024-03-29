FROM python:3.11

RUN mkdir /src

COPY ./src /src

WORKDIR /src

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["./docker-entrypoint.sh"]
FROM python:3.10-bookworm

RUN pip install -U pip poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY src ./src
COPY gunicorn.conf.py ./

CMD ["poetry", "run", "gunicorn", "src.wsgi:create_app()"]

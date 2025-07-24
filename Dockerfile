FROM python:3.11

# Set the working directory in the container
RUN pip install --root-user-action=ignore --upgrade pip && \
    pip install --root-user-action=ignore poetry

ENV APP_ROOT=/app
ENV PYTHONPATH=${APP_ROOT}
WORKDIR ${APP_ROOT}

ENV POETRY_VIRTUALENVS_PATH=/tmp/poetry-cache

COPY pyproject.toml poetry.lock ${APP_ROOT}/
RUN poetry install --no-interaction --no-root $(test -f pyproject.toml && grep -q 'tool.poetry.group.dev' pyproject.toml && echo "--without dev" || true)


COPY . ${APP_ROOT}

CMD ["poetry", "run", "python", "-m", "app.main"]

FROM python:3.10-buster as py-build

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -

COPY . /app
WORKDIR /app
ENV PATH=/opt/poetry/bin:$PATH
RUN poetry config virtualenvs.in-project true && poetry install

FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    libmediainfo-dev

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
COPY --from=py-build /app /app
WORKDIR /app
ENTRYPOINT [".venv/bin/python", "-m", "streamlit", "run", "mtcc/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
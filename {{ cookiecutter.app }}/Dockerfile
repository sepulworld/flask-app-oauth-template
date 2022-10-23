FROM python:3.10.4-buster

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.13 

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
RUN useradd {{ cookiecutter.app }} 

WORKDIR /home/{{ cookiecutter.app }}

COPY poetry.lock pyproject.toml /home/{{ cookiecutter.app }}

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY app app
COPY migrations migrations

COPY {{ cookiecutter.app }}.py config.py boot.sh ./
RUN chmod a+x boot.sh
RUN chown -R {{ cookiecutter.app }}:{{ cookiecutter.app }} ./
USER {{ cookiecutter.app }} 

EXPOSE 5000/tcp

ENV FLASK_APP {{ cookiecutter.app }}.py
ENV PYTHONPATH=/app/
ENTRYPOINT ["./boot.sh"]

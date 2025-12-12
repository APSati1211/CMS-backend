FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# install deps
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

# copy code
COPY . /app

# collect static files (if set up) and run migrations
# NOTE: fixed typo "migarte" -> "migrate". Use "|| true" to avoid hard build failure on DB absence.
RUN python manage.py collectstatic --noinput || true \
 && python manage.py makemigrations || true \
 && python manage.py migrate --noinput || true

EXPOSE 8000

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--log-level", "info"]

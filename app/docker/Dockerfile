FROM python:3.7-alpine
WORKDIR /app
RUN apk add --no-cache gcc g++ musl-dev linux-headers
RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    mariadb-dev \
    python3-dev \
    postgresql-dev \
    ;
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN alembic init alembic
EXPOSE 5000
COPY . .
CMD ["python", "app.py"]

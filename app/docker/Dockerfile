FROM python:3.7-alpine
WORKDIR /app
RUN apk add --no-cache gcc g++ musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install alembic
RUN alembic init alembic
EXPOSE 5000
COPY . .
CMD ["python", "app.py"]

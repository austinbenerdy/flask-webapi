FROM python:3.7-alpine
WORKDIR /
RUN apk add --no-cache gcc g++ musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "app.py"]

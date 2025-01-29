FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 7005

CMD ["flask", "run"]
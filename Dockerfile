FROM python:3.7

COPY . /app

RUN pip3 install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]

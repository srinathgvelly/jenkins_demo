FROM python:3.7

COPY . /app
COPY requirements.txt ./
RUN pip install -y -r requirements.txt
COPY ./"dir"/* .
EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]

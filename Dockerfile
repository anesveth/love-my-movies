FROM python:3-alpine

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app
ENTRYPOINT ["python"]
CMD ["lmm.py"]

EXPOSE 5000
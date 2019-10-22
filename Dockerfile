FROM python:3-alpine

WORKDIR /lovemymovies
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install certifi
RUN pip install --upgrade certifi

COPY . ./
CMD ["sudo apt-get install redis-server"]
CMD ["sudo service redis-server start"]
CMD [ "python", "lmm.py" ]

EXPOSE 5000
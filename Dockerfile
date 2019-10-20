FROM python:3-alpine

WORKDIR /lovemymovies
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

CMD [ "python", "lmm.py" ]

EXPOSE 5000
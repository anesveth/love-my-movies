FROM python:3-alpine

WORKDIR /lovemymovies
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install certifi
RUN pip install --upgrade certifi

COPY . ./
CMD start.sh
CMD [ "python", "lmm.py" ]

EXPOSE 5000
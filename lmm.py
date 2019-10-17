from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests,json,sys,os
app=Flask(__name__)

url="https://api.themoviedb.org/3/movie/550?api_key=8728b5dc931038ddc249435581c9d555"

@app.route("/")
def home():
    return render_template('layout.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=70,debug=True)
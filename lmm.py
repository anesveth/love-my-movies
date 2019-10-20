from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests,sys,csv,json
app=Flask(__name__)

apikey="8728b5dc931038ddc249435581c9d555"
url=f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"

try:
    html_stuff=requests.get(url).text
except:
    print("Unnable to access api")
    sys.exit(1)

# Parse the html content
soup = BeautifulSoup(html_stuff, "html.parser")
def jsonify(html_stuff):
    with open(html_stuff) as json_file:
        data = json.load(json_file)
        return data
        
@app.route("/")
def home():
    # maxmovies=0;
    # movies=[]
    # data=jsonify(html_stuff)
    # for movie in data['results']:
    #     if maxmovies<=6:
    #         movies.append(movie)
    #         maxmovies+=1;
    return render_template('layout.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
from flask import Flask, render_template
import requests,sys,csv,json
import redis
from urllib.request import urlopen
app=Flask(__name__)

apikey="8728b5dc931038ddc249435581c9d555"
url=f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"

try:
    data=requests.get(url)
except:
    print("Unnable to access api")
    sys.exit(1)


# def jsonify(html_stuff):
#     with open(html_stuff) as json_file:
#         data = json.load(json_file)
#         return data
# r = redis.StrictRedis(host='localhost', port=6379, db=1)
# r.set('data',html_stuff)

# response = urlopen(url)
# data = response.read().decode("utf-8")
# dictdata= json.loads(data)

@app.route("/")
def home():
    maxmovies=0;
    movies=[]
    # data=jsonify(r.get('data'))
    for movie in data.json()['results']:
        if maxmovies<=6:
            movies.append(movie)
            maxmovies+=1;
    return render_template('layout.html',movies=movies)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
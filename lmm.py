from flask import Flask, render_template
import requests,sys,csv,json
import redis

app=Flask(__name__)

apikey="8728b5dc931038ddc249435581c9d555"
url=f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"

try:
    api=requests.get(url)
except:
    print("Unnable to access api")
    sys.exit(1)

r = redis.StrictRedis(host='docker.for.mac.localhost', port=6379)
# def jsonify(html_stuff):
#     with open(html_stuff) as json_file:
#         data = json.load(json_file)
#         return data


movies=api.json()['results']

# response = urlopen(url)
# data = response.read().decode("utf-8")
# dictdata= json.loads(data)

@app.route("/")
def home():
    maxmovies=0;
    counter4hiding=0
    popular=[]
    discover=[]
    overfloww=[]
    rdictionary={}
    longtitle=[]
    for movie in movies:
        for item,value in movie.items():
                if item=='overview':
                    if len(value)>200:
                        overfloww.append(movie)
                if item=='original_title':
                    if len(value)>33:
                        longtitle.append(movie)
                        
                if item!='video' or item!='adult' or item!='genre_ids':
                    rdictionary[item]=str(value)
        if maxmovies<=6:
            popular.append(movie)
            maxmovies+=1;
        else:
            discover.append(movie)
        title=str(movie['original_title'])
        r.hmset(title,rdictionary)
    return render_template('layout.html',popular=popular,overfloww=overfloww,discover=discover,longtitle=longtitle,moviecounter=counter4hiding)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
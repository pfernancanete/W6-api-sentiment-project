from flask import Flask, request
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos


app = Flask(__name__)


## GET ##

# Este endpoint hace referencia al README. 
@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"]
    )
    return md_template_string


# Endpoint 1 - Retweets
@app.route("/retweetspop/<numberrt>")
def retweetnumb(numberrt):
    print(f"el numero es {numberrt}")
    print("getting tweets")
    tweets = get.retweetnumb(int(numberrt))
    return json.dumps(tweets)


# Endpoint 2 - Favourites #
@app.route("/favourites/<favs>")
def favtweet(favs):
    tweets_fav = get.mayores_favoritos(int(favs))
    return json.dumps(favtweet)


# Endpoint 3 - Year #
@app.route("/yeartweets/<yeart>")
def yeartweet(yeart):
    year0 = yeart.split(" ")[0]
    year1= yeart.split(" ")[1]
    
    yeartweet = get.yeartweet(year0, year1)
    return json.dumps(yeartweet)  


# Endpoint 4 - Polarity #
@app.route("/polarity/<year>")

def avg_polarity(year):
    mean_anual_polarity = avg_polarity2(year)
    return json.dumps(mean_anual_polarity)



## POST ##

@app.route("/newtweet/", methods=["POST"])
def insertnuevotweet():
    tweet = request.form.get('content')
    retweet = request.form.get('retweets')
    favoritos = request.form.get('favorites')
    año = request.form.get('year')
    
    pos.insertnuevotweet(tweet, retweet, favoritos, año)
    return "Message introduced succesfully on the database"











app.run("0.0.0.0", 5000,debug=True)


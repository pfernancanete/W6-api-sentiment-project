from config.configuration import db, collection
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def mayoresretweets(numero):
    """
   Función que devuelve los tweets con x numero de retweets
    """
    query_one = {'rt': {"$gt": numero}}
    print(query_one)
    tweets = list(collection.find(query_one,{"tweet": 1, "rt": 1, "_id" : 0}))   
    return tweets



def mayores_favoritos(numero):
    """
   Función que devuelve los tweets con x numero de favoritos
    """
    query_two = {'favourites':{"$gt": numero}}
    tweets_fav = list(collection.find(query_two, {"tweet": 1, "favourites": 1, "_id" : 0}))
    return tweets_fav


def year_tweets(year0, year1):
    """
   Función que devuelve los tweets de un año en concreto
    """    
    query_third = {"$and":[{'year': {"$gt": year0}}, {'year': {"$lt": year1}}]}
    year_tweets = list(collection.find(query_third, {"tweet": 1, "year":1, "_id": 0}))
    return year_tweets



def polaridad_media2(year):
    query_fourth = {'year': year}
    year = list(collection.find(query_fourth, {"tweet": 1, "_id" : 0}))
    
    
    sia = SentimentIntensityAnalyzer()

    
    pos = []
    for i in year:
        polarity = sia.polarity_scores(i['tweet'])
        pos.append(polarity['pos'])
    

    mean_anual_polaridad = sum(pos)/len(pos)
    print(mean_anual_polaridad)
    return mean_anual_polaridad

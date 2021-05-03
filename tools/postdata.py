from config.configuration import db,collection

def insertnuevotweet(tweet, rt, favourites, año):
    """
    This function will input the data to MongoDb as we want.
    """

    dict_insert = {"tweet" : f"{tweet}",
    "retweets" : f"{rt}",
    "favourites" : f"{favourites}",
    "year" : f"{year}"
    }

    collection.insert_one(dict_insert)
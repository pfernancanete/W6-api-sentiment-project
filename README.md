# W6-api-sentiment-project

![DT](https://user-images.githubusercontent.com/80899361/116906153-31e66800-ac40-11eb-9a34-d844acd68df8.jpg)


This is the fifth project I do at the Data Analytics bootcamp in Ironhack.

## Purpose
The purpose of this project is to create an API that:

1. Serves information to clients (in response to their GET requests).
2. Receives data from your clients (via their POST requests) and saves it to your own database.

## Method
We have selected a very clean dataset from Kaggle.com, of several tweets of the polemic ex president of the United States, Donald Trump. We have settled and cleaned the dataset with python libraries such as Pandas and when ready, we've imported it to MongoDB to create the API calls. To do so, we've used Flask.

- GET requests: we've created four endpoints, so anyone can access the data with a single call.

- POST requests: we've imported the data to our database in MongoDB with a single call.

Moreover, we've done a polarity analysis to determine whether the tweets had a positive or a negative tone.


## Libraries and tools:
- MongoDB
- Python: pandas, json, nltk, requests, pymongo
- Dillinger (README)
- Kaggle.com
- Flask
- Visual Code

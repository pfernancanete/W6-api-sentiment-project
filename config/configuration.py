"""
Connection to MongoDB
"""

import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv("URL")

# We make sure it has connected to MongoDB #
if not (DBURL):
    raise ValueError("no MongoDB URL")

client = MongoClient(DBURL)
db = client.get_database()
collection = db["tweets"]
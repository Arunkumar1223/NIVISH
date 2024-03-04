import pymongo
from database import x
import urllib.parse
def mongoqueryfun():
    username = x['default']
    a = x['default']['NAME']

    try:
        Username = (username['CLIENT']['username'])
        password = (username['CLIENT']['password'])
        escaped_username = urllib.parse.quote_plus(Username)
        escaped_password = urllib.parse.quote_plus(password)
        print("--------------------staging----------------------------------------")
        myclient = pymongo.MongoClient(f"mongodb://{escaped_username}:{escaped_password}@{username['CLIENT']['host']}:27017/")
    except:
        print("--------------------local----------------------------------------")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[a]

    # print(mydb)
    return mydb
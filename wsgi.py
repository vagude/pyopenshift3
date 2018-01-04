from flask import Flask
from pymongo import MongoClient
import os

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"
    
@application.route("/save/mongo")
def saveInMongo():
    host = os.getenv('MONGODB_SERVICE_HOST')
    port = os.getenv('MONGODB_SERVICE_PORT')
    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_PASSWORD')
    db = os.getenv('MONGO_SCHEMA')

    #mongodb://root:pass@localhost:27017/
    conn = MongoClient('mongodb://{}:{}@{}:{}/'.format(username, password, host, port))
    db = conn['{}'.format(db)]
    coll = db['employee']
    coll.save({"_id" : 1, "name" : "Vamsi", "address" : "San Jose"})

    return "{} - {} - {} - {} - {}".format(host, port, username, password, db)


if __name__ == "__main__":
    application.run()
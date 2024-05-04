from flask import Flask
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB connection

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
db = PyMongo(app).db
@app.route('/')
def home():
    db.inventory.insert_one({"name": "parth"})

    # Retrieve data from MongoDB
    # data = db.mycollection.find()
    return "<h1> Hello World </h1>"

    # Process the data and render a template
    # return f"Data from MongoDB: {list(data)}"

if __name__ == '__main__':
    app.run(debug=True)
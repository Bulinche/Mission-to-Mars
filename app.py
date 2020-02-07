from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars
import sys

sys.setrecursionlimit(2000)
app = Flask(__name__)

# client = pymongo.MongoClient()
# db = client.mars_db
# collection = db.mars_facts

# Routes
@app.route('/scrape')
def scrape():
    mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
    
    mars_data = scrape_mars.scrape()
    mars = mongo.db.mars
    mars.update({}, mars_data, upsert=True)
    
    return redirect("http://localhost:5000/", code=302)

@app.route("/")
def index():
    mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

if __name__ == "__main__":
    app.run(debug=True)
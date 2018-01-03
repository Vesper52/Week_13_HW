from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def index():
    scrapping = mongo.db.scrapping.find_one()
    return render_template('index.html', scrapping=scrapping)

@app.route('/scrape')
def scrape():
    scrapping = mongo.db.scrapping
    scrapping_data = scrape_mars.scrape()
    scrapping.update(
    {},
    scrapping_data,
    upsert=True
    )
    return redirect('http://localhost:27017/', code=302)

if __name__ == "__main__":
    app.run(port=27017,debug=True)

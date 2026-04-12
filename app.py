from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient(MONGO_URI)
db = client["testdb"]
collection = db["users"]

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        with open('data.json', 'r') as file:
            data = json.load(file)

        # Step 2: Add new data
        new_entry = {
            "name": name,
            "email": email
        }
        data.append(new_entry)

        # Step 3: Write back to file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/api', methods = ['GET'])
def get_data():

    with open('data.json') as file:
        data = json.load(file)

        return jsonify(data)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
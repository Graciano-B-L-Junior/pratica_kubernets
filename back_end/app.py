from quotes import printQuote
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def start():
    quotes = printQuote()
    response = jsonify(quotes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
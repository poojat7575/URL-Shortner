from flask import Flask, request
from flask import jsonify
app = Flask(__name__)
database = {}

@app.route("/", methods = ["GET"])
def home():
    return "Welcome to url shortner app"

@app.route("/short_url", methods = ["PUT"])
def short_url():
    long_url = request.json.get("url")
    base_url = long_url.partition('.com/')[0] + '.com'
    short_url = '/'
    for i in range(10):
        short_url += chr(random.randint(ord('a'), ord('z')))
    base_url += short_url
    database[base_url] = long_url
    return jsonify("".join(base_url))

@app.route("/long_url", methods = ["PUT"])
def long_url():
    short_url = request.json.get("url")
    return jsonify(database.get(short_url, "No records found"))


if __name__ == "__main__":
    app.run()

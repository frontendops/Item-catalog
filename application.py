from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/", methods=['GET'])
def home():
    return jsonify("Greetings from python!!")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
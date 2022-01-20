from flask import Flask, request, jsonify
from data import data

app = Flask(__name__)


@app.route('/')
def main():
    return jsonify({"data": data, "status": "200 ok"})


@app.route("/planetName")
def getData():
    planetName = request.args.get("name")
    result = next(item for item in data if item["name"] == planetName)
    if len(result) == 0:
        return "just go and die"
    else:
        return jsonify({"result": result, "status": "200 ok"})


if __name__ == '__main__':
    app.run(debug=True)

from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/reverse_sentence", methods=['POST'])
def reverse_sentence():
    sentence = request.get_json()['sentence']
    polarity = sentence[::-1]
    return jsonify(
        sentence=sentence,
        polarity=polarity
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

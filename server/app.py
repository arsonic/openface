from flask import Flask
from flask import request
from flask import jsonify
import os
import sys
sys.path.append('/openface/demos/')
import classifier

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test", methods=['POST'])
def test():
    return jsonify(**{'name': 'jake_johnson', 'confidence': 0.1})

@app.route("/classify", methods=['POST'])
def classify():
    file = request.files['image']
    filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images/image.png')
    file.save(filePath)
    modelPath = '/openface/images/actors_features/classifier.pkl'
    result = classifier.inferWithParams({'img': filePath, 'classifierModel': modelPath})
    return jsonify(**result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

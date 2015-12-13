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
    return "Actorzam server v0.1"


@app.route("/test", methods=['POST'])
def test():
    """
    Endpoint used for debugging.
    Returns a JSON in the same format as the /classify endpoint
    """
    return jsonify(**{'name': 'jake_johnson', 'confidence': 0.1})

@app.route("/classify", methods=['POST'])
def classify():
    """
    Accepts an image in a POST request (in the 'image' key), classifies it
    and returns a JSON of the format {'name': name_of_the_actor, 'confidence': 0.4},
    where name_of_the_actor corresponds to the name of the actor on the image
    and confidence - the confidence of the classification task
    """

    # Extract image:
    file = request.files['image']
    filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images/image.png')
    file.save(filePath)

    # Load model:
    modelPath = '/openface/images/actors_features/classifier.pkl'

    # Classify image:
    result = classifier.inferWithParams({'img': filePath, 'classifierModel': modelPath})
    return jsonify(**result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

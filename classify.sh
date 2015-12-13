#!/bin/sh

image=$1

if [ -z "$image" ]; then
        echo "Usage: ./classify.sh path/to/image.png"
	echo "Classifying image ./images/actors_tests/zoo1.jpg"
	image="/openface/images/actors_tests/zoo1.jpg"
fi

# The script uses classifier.py script from the openface repository
# ./images/actors_features/classifier.pkl is the path to the finetuned
# model
./demos/classifier.py infer ./images/actors_features/classifier.pkl $image

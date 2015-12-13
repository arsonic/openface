#!/bin/sh

image=$1

./demos/classifier.py infer ./images/actors_features/classifier.pkl $image

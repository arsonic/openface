#!/bin/sh

# Preprocess images:
for N in {1..4}; do 
  ./util/align-dlib.py images/actors align affine images/actors_aligned --size 96 
done

# Generate representations:
./batch-represent/main.lua -outDir images/actors_features -data images/actors_aligned

# Train:
./demos/classifier.py --verbose train images/actors_features 

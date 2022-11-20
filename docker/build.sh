#!/bin/bash

# Build and tag Python 2.7 images
docker build --build-arg PYTHON_VERSION=2.7 -t jgtpyalgotrade:0.20 .
docker tag jgtpyalgotrade:0.20 jgtpyalgotrade:0.20-py27
docker tag jgtpyalgotrade:0.20 gbecedillas/jgtpyalgotrade:0.20
docker tag jgtpyalgotrade:0.20-py27 gbecedillas/jgtpyalgotrade:0.20-py27

# Build and tag Python 3.7 images
docker build --build-arg PYTHON_VERSION=3.7 -t jgtpyalgotrade:0.20-py37 .
docker tag jgtpyalgotrade:0.20-py37 gbecedillas/jgtpyalgotrade:0.20-py37

# Push images
docker login --username=gbecedillas
# docker push gbecedillas/jgtpyalgotrade:0.20
docker push gbecedillas/jgtpyalgotrade:0.20-py27
docker push gbecedillas/jgtpyalgotrade:0.20-py37

# docker rmi $(docker images --quiet --filter "dangling=true")

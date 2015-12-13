#!/bin/sh

docker run -p 80:80 -t -i -v $PWD:/openface openface /bin/bash

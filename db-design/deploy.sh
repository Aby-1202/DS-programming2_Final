#!/bin/sh

################################################################################
#
# deploy.sh for AI-TECH
# (C) Yasuhiro Hayashi
#
################################################################################

USERNAME=$(whoami)
HOST_PATH="/Users/$USERNAME"
PROJECT_NAME="db-design"
PROJECT_TAG="0.1" # latest or specific version

################################################################################

rm deploy/flaskdb.tar.gz
tar cfvz deploy/flaskdb.tar.gz --exclude __pycache__ --exclude ".DS_Store" flaskdb

CONTAINER_ID=`docker ps -a | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 1`
if [ "$CONTAINER_ID" != "" ]; then
    docker stop $CONTAINER_ID; wait
    docker rm $CONTAINER_ID; wait
fi

IMAGE_ID=`docker images | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 3`
if [ "$IMAGE_ID" != "" ]; then
    docker rmi $IMAGE_ID; wait
fi

docker builder prune -a
docker build -t $PROJECT_NAME:$PROJECT_TAG .
docker run -it -p 18080:8080 -p 15432:5432 -v $HOST_PATH/$PROJECT_NAME/flaskdb:/flaskdb $PROJECT_NAME:$PROJECT_TAG
#docker run -it -p 18080:8080 -p 15432:5432 -v c:\\$PROJECT_NAME\\flaskdb:/flaskdb $PROJECT_NAME:$PROJECT_TAG

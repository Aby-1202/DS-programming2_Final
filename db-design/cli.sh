#!/bin/sh

################################################################################
#
# flaskdb.sh for AI-TECH
# (C) Yasuhiro Hayashi
#
################################################################################

USERNAME=`whoami`

HOST_PATH="/Users/$USERNAME"
PROJECT_NAME="db-design"
PROJECT_TAG="0.1" # latest or specific version

################################################################################

CONTAINER_ID=`docker ps -a | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 1`
if [ "$CONTAINER_ID" != "" ]; then
    docker start $CONTAINER_ID; wait
fi

docker exec -it -w /flaskdb $CONTAINER_ID bash

#!/bin/bash
set -e

# Stop the running container (if any)
contained_id=`docker ps | aws -F " " '{print $1}'`
docker rm -f $container_id

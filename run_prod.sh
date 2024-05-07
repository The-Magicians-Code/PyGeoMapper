#!/usr/bin/env bash
# @Author: Tanel Treuberg
# @Github: https://github.com/The-Magicians-Code
# @Description: Build and run Python production development container

tag="pygeomapper_prod"
name="geomap_prod"

docker build -t "$tag" . -f Dockerfile.prod
docker run --rm -it -d -p 80:8061 --name "$name" "$tag"
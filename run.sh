#!/usr/bin/env bash
# @Author: Tanel Treuberg
# @Github: https://github.com/The-Magicians-Code
# @Description: Build and run R development container

tag="pygeomapper"
name="geomap"

docker build -t "$tag" . -f Dockerfile
docker run --rm -it -d -v $(pwd):/src -p 80:8061 --name "$name" "$tag"
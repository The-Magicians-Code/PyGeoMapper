#!/usr/bin/env bash
# @Author: Tanel Treuberg
# @Github: https://github.com/The-Magicians-Code
# @Description: Build and run Python dev development container

tag="pygeomapper_dev"
name="geomap_dev"

docker build -t "$tag" . -f Dockerfile.dev
docker run --rm -it -d -v $(pwd):/src -p 3000:8061 --name "$name" "$tag"
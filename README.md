# PyGeoMapper
Calculate the distance of multiple points from a primary coordinate and display results on a web interface with a downloadable map. The application is being developed and deployed in a Docker environment. This repository consists of development and production container scripts, source code within [/src](/src/) folder and relevant data source in [/data](/data/) folder. Example of an exported [interactive map](https://the-magicians-code.github.io/PyGeoMapper/)
>Current implementation is MVP, see [issues](https://github.com/The-Magicians-Code/PyGeoMapper/issues)
## Configure and run
Install [docker](https://docs.docker.com/get-docker/)  
Run dev or prod environment from the terminal
````
bash run_{dev/prod}
````
Display running containers
````
docker ps
````
Connect to the container terminal using the container name and desired terminal
````
docker exec -it container_name bash
````
Stop the container process
````
docker stop container_name
````
### Notes
Info on system compatability  
>https://developers.arcgis.com/python/guide/system-requirements/

Branch [`gh-pages`](https://github.com/The-Magicians-Code/PyGeoMapper/tree/gh-pages) is a copy of the main branch and used for hosting the [`map`](https://github.com/The-Magicians-Code/PyGeoMapper/blob/main/index.html) file named with the required name of `index.html` on GitHub Pages

# Demo_ML_Project
This is machine learning project

1. HEROKU_EMAIL=
2. HEROKU_API_KEY=
3. HEROKU_APP_NAME= 

BUILD_DOCKER_IMAGE
```
docker build -t <image name>:<tagname> .
```
>Note: Image name for docker must be lowercase

To list docker image
```
docker images
```
Run docker image: 
```
docker run -p 5000:5000 -e PORT=5000 52b200c216a1
```
To check running container in docker
```
docker ps
```
to stop any docker conatiner
```
docker stop <container_id>
## Building the Docker Container

```
$ docker build -f Dockerfile -t $DOCKER_USER_ID/bp-pythonservice .
```

## Running the Docker Container

```
$ docker run -d -p 5050:5000 $DOCKER_USER_ID/bp-pythonservice
```

The app is listening by default on port 5000. The 5050 port of the host machine is mapped to the port 5000 of the container.

-p 5050:5000 i.e.


## Pushing to Docker Hub

```
$ docker push $DOCKER_USER_ID/bp-pythonservice
```

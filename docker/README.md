# Docker container connection
## 1. Docker compose CLI
To install `docker-compose` on linux :
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```
Note, the docker-compose file must in name `docker-compose.yml` or `docker-compose.yaml` in the root directory of the project.
Below commands are used to start the docker container, same as `docker run` command.
```
docker-compose up
```
Below command is used to build and start the docker container, same as `docker build` and `docker run` command.
```
docker-compose --build
```
stop the container
```
docker-compose down
```
restart policy in `docker-compose.yml` file
- `no` : never restart
- `always` : always restart
- `on-failure` : restart only when container fails
- `unless-stopped` : restart unless stopped by user


## 2. Docker Network


# Docker Swarm
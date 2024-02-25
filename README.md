
# Kubernetes
Open-source container orchestration platform, help to mange cotainers at scale.  
- `orchestration` : The process of automating the deployment, scaling, and management of containerized applications.
    - high availability or no downtime
    - scalability or high performance
    - disaster recovery
- trend from monolithic to microservices architecture.

## K8s Components
- `pod`: This is the basic unit in the k8s.
- `service`: Service is used to expose the pod to the outside world. In service, one typical type is load balancer.
- `Ingress`: Ingress is used to expose the service to the outside world.
- `deployment`: Deployment is used to manage the pod. It is used to create, update, and delete the pod.
- `Volume`: Volume is used to store the data. It is used to make the data persistent.
- `StatefulSet`: StatefulSet is used to manage the stateful application.
- `Secret`: Secret is used to store the sensitive information like password, token, etc.
- `ConfigMap`: ConfigMap is used to store the configuration information.


# Docker
- docker image : This is the basic unit in the docker. It is a snapshot of the file system.
- docker container : This is the running instance of the docker image.
- Docker vs VM
    - Containerization vs. Virtualization: Docker containers run on the host OS sharing the same kernel, making them lightweight. In contrast, VMs include full copies of an OS, a hypervisor, and the application, making them heavier.
    - Performance: Docker's approach ensures applications use fewer resources than VMs, offering faster start-up times and better performance.
    - Isolation Level: Docker provides application-level isolation, whereas VMs provide OS-level isolation.

## ocker Commands
### Essential Commands
- `docker build` : Builds Docker images from a Dockerfile and a context.
```
docker build -t <IMAGE_NAME>:<TAG> .
```
- `docker run` : Runs a Docker container from an image.
    - detach mode with port mapping: `-d -p <EXTERNAL_PORT>:<INTERNAL_PORT>`
```
docker run -d -p <EXTERNAL_PORT>:<INTERNAL_PORT> \
    -e <ENV_NAME>=<VALUE> -v <HOST_DIR>:<CONTAINER_DIR> \
    --name <CONTAINER_NAME> <IMAGE_NAME>:<TAG>
```
    - iterative mode: `-it` for troubleshooting
```
docker run -it -p <EXTERNAL_PORT>:<INTERNAL_PORT> \
    -e <ENV_NAME>=<VALUE> -v <HOST_DIR>:<CONTAINER_DIR> \
    --name <CONTAINER_NAME> <IMAGE>
```
    - user `-v` to mount the volume, make data persistent.

### Other Commands
- `docker ps` : Lists running containers.
- `docker images` : Lists all Docker images on the host.
- `docker exec` : Executes a command inside a running container.
```
docker exec -it <CONTAINER_NAME_OR_ID> /bin/bash
```
- `docker logs` : Fetch the logs of a container.
```
docker logs <CONTAINER_NAME_OR_ID>
```
- `docker start`
```
docker start <CONTAINER_NAME_OR_ID>
```
- `docker stop`
```
docker stop <CONTAINER_NAME_OR_ID>
```

## DOCKERFILE
```
FROM <BASE_IMAGE>
WORKDIR <WORKING_DIRECTORY>
ENV <ENV_NAME>=<VALUE>
COPY <SOURCE> <DESTINATION>
CMD <COMMAND>
```

## docker compose
for running multiple containers


## docker network


## docker swarm



# References
- [Docker Kubernetes Udemy Course](https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/)
- [k8s notes](https://kubernetes.io/docs/home/)
- [Docker](https://docs.docker.com/)
- [Alex Chen Notes](https://github.com/alexchen4ai/KubernetesNotes)
- TechWorldwithNana
    - [Docker](https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana)
    - [K8S](https://www.youtube.com/watch?v=X48VuDVv0do&ab_channel=TechWorldwithNana)

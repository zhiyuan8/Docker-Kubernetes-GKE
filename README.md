
# Kubernetes
Open-source container orchestration platform, help to mange cotainers at scale.  
- `orchestration` : The process of automating the deployment, scaling, and management of containerized applications.
    - high availability or no downtime
    - scalability or high performance
    - disaster recovery
- trend from monolithic to microservices architecture.

## K8s Components
### contrainer abtraction
- `pod`: This is the basic unit in the k8s, usually 1 application per pod.
    - earch pod has its own IP address, use internal IP address
    - new IP address when pod restarts
- `service`: Service is used to expose the pod to the outside world. In service, one typical type is load balancer.
    - persistent IP address
    - lifecycle of pod and service are independent
    - load balancer : distribute the traffic to the pods
- `Volumes`: For **data storage**. It is used to make the data persistent.
    - attach physical storage to the pod, or remote storage
    - k8s does **NOT** persist data by default

### route traffic in cluster
- `Ingress`: Manages external access to the services in a cluster, providing HTTP and HTTPS routing.
- `k8s cluster`: A k8s cluster is a set of nodes that run containerized applications. 
    - `master node`: The master node is responsible for managing the cluster.
    - `worker node`: The worker node is responsible for running the application.

### external configuration
- `ConfigMap`: ConfigMap is used to store the configuration information.
    - store external configuration of your application
    - don't put sensitive information, put them in `Secret`
- `Secret`: Secret is used to store the sensitive information like password, token, etc. in base64 encoded format.


### Replicating mechanism
- `deployment`: create, update, and delete the pod.
    - user creates the deployment, and deployment creates the pod
    - `deployment` is used to manage the **stateless** application
- `StatefulSet`: StatefulSet is used to manage the stateful application and avoid data inconsistency, such as `database`.
    - `StatefulSet` is used to manage the **stateful** application
    - host DB outside of the k8s cluster because it is diffucult to manage the stateful application in k8s cluster.

## K8s Architecture
3 process : 1. Kube proxy, 2. Kubelet, 3. Kube API server
usually 2 master nodes for high availability, and 3 worker nodes for high performance.

master process :
client request -> Kube API server ->  Kube scheduler -> Kube controller manager -> etcd (key-value store), cluster brain

worker process :

Add new master / node server
1. get new bare server
2. install all the master / worker node processes
3. join the new server to the cluster

## minikube and kubectl
test / local cluster setup : master and worker node run in one machine

kubectl : command line tool to interact with k8s cluster

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
- [k8s official website](https://kubernetes.io/docs/home/)
    - [installation](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
- [Docker official website](https://docs.docker.com/)
- [Alex Chen Notes](https://github.com/alexchen4ai/KubernetesNotes)
- TechWorldwithNana
    - [Docker](https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana)
    - [K8S](https://www.youtube.com/watch?v=X48VuDVv0do&ab_channel=TechWorldwithNana)

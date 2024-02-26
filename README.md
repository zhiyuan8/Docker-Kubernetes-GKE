
# Kubernetes
Open-source container orchestration platform, help to mange cotainers at scale.  
- `orchestration` : The process of automating the deployment, scaling, and management of containerized applications.
    - high availability or no downtime
    - scalability or high performance
    - disaster recovery
- trend from `monolithic` to `microservices` architecture.
    - `monolithic` : all the services are in one application
    - `microservices` : each service is in one application, and communicate with each other.

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
Usually 2 master nodes for high availability, and 3 worker nodes for high performance.

### Master Nodes
Components:
- `Kube API Server`: Acts as the front-end for the Kubernetes control plane. It is the primary management point of the entire cluster, handling user requests, and operations within the cluster.
- `Kube Scheduler`: Watches for newly created Pods with no assigned node, and selects a node for them to run on based on resource availability, constraints, and other policies.
- `Kube Controller Manager`: Runs controller processes. It watches the state of the cluster through the API server and makes changes attempting to move the current state towards the desired state.
- `etcd`: A consistent and highly-available key-value store used as Kubernetes' backing store for all cluster data. It represents the state of the cluster at any given point in time.

### Worker Nodes
Components:
- `Kubelet`: An agent that runs on each worker node in the cluster. It makes sure that containers are running in a Pod.
- `Kube-proxy`: Maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster.
- `Container Runtime`: The software that is responsible for running containers. Kubernetes supports several container runtimes, such as Docker, containerd, and CRI-O.

### Adding New Masters or Worker Nodes
1. Obtain a new bare-metal server or virtual machine.
2. Install the necessary components for a master or worker node. This includes installing a container runtime, kubelet, kube-proxy, and for master nodes, the Control Plane components.
3. Join the new server to the cluster using the Kubernetes join command, which requires a token and the address of the Control Plane's API server.

# Docker
For `docker compose` and `docker network` and `docker swarm`, see [readme](docker/README.md)

- Docker image: A snapshot of the filesystem, serving as Docker's basic unit.
- Docker container: A running instance of a Docker image.
- Docker vs VM:
    - Docker containers **share the host OS kernel**, making them lightweight and fast. VMs contain full OS copies, are heavier, and have slower startup times.
    - Docker offers **application-level isolation**; VMs provide **OS-level isolation**, enhancing security but at a resource cost.

## Docker Commands
### Essential
- `docker build` : Builds Docker images from a Dockerfile and a context.
```
docker build -f <DOCKER_FILE> -t <IMAGE_NAME>:<TAG> .
```
If you want to build for dev environment, use `Dockerfile.dev` instead of `Dockerfile`.
- `docker run` : Runs a Docker container from an image.
    - detach mode with port mapping: `-d -p <EXTERNAL_PORT>:<INTERNAL_PORT>`
    - iterative mode: `-it` for troubleshooting
    - user `-v` to mount the volume, make data persistent.
```
# detached
docker run -d -p <EXTERNAL_PORT>:<INTERNAL_PORT> \
    -e <ENV_NAME>=<VALUE> -v <HOST_DIR>:<CONTAINER_DIR> \
    --name <CONTAINER_NAME> <IMAGE_NAME>:<TAG>
# iterative
docker run -it -p <EXTERNAL_PORT>:<INTERNAL_PORT> \
    -e <ENV_NAME>=<VALUE> -v <HOST_DIR>:<CONTAINER_DIR> \
    --name <CONTAINER_NAME> <IMAGE>
```

### Others
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

## DOCKERFILE format
```
FROM <BASE_IMAGE>
WORKDIR <WORKING_DIRECTORY>
ENV <ENV_NAME>=<VALUE>
COPY <SOURCE> <DESTINATION>
CMD <COMMAND>
```

**Dev dockerfile**
for React, distingish between development and production environment. Generate `Dockerfile.dev` for development environment.

# References
- [Docker Kubernetes Udemy Course](https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/)
- [k8s official website](https://kubernetes.io/docs/home/)
    - [installation](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
- [Docker official website](https://docs.docker.com/)
- [Alex Chen Notes](https://github.com/alexchen4ai/KubernetesNotes)
- TechWorldwithNana
    - [Docker](https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana)
    - [K8S](https://www.youtube.com/watch?v=X48VuDVv0do&ab_channel=TechWorldwithNana)

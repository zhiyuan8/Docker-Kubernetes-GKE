# Kubernetes Commands
CRUD operations
- create deployment / multiple pods
  - `kubectl create deployment <DEPLOYMENT_NAME> --image=<IMAGE_NAME>:<TAG>`
- edit deployment
  - `kubectl edit deployment <DEPLOYMENT_NAME>`
- delete deployment
  - `kubectl delete deployment <DEPLOYMENT_NAME>`
- status of different k8s components
  - `kubectl get all`
  - `kubectl get pods`
  - `kubectl get services`
  - `kubectl get deployments`
  - `kubectl get replicaset`

DUBUGGING
- logs
  - `kubectl logs <POD_NAME>`
- exec
  - `kubectl exec -it <POD_NAME> -- bin/bash`


# miniKube commands
Just for start up / shut down / delete cluster
```
minikube start
```
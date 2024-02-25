# Create a sample deployment and expose it on port 8080:
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080

# launch the service in the browser
minikube service hello-minikube

# another way, can open localhost:7080 in the browser
kubectl port-forward service/hello-minikube 7080:8080
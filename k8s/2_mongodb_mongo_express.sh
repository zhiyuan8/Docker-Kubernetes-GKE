kubectl apply -f 2_mongodb_mongo_express_secret.yaml
# print the secret
kubectl get secret

kubectl apply -f 2_mongodb_mongo_express.yaml
# print all
kubectl get all
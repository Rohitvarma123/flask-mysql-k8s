# Flask + MySQL on Kubernetes

This project demonstrates a 2-tier app using Flask (Python) and MySQL on Kubernetes.

## Usage

kubectl apply -f mysql-secret.yaml
kubectl apply -f mysql-pvc.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f flask-deployment.yaml

Then visit:
http://<minikube-ip>:30008

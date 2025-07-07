# Flask + MySQL on Kubernetes

This project demonstrates a 2-tier app using Flask (Python) and MySQL on Kubernetes.

## Usage

kubectl apply -f mysql-secret.yaml
kubectl apply -f mysql-pvc.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f flask-deployment.yaml

✅ Step 3: Build and Push Flask Image
docker build -t your_dockerhub/flask-mysql-demo:latest .
docker push your_dockerhub/flask-mysql-demo:latest



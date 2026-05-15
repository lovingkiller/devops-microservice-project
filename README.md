# Devops Microservice Deployment Project

This repository demonstrate an end-to-end local CI/CD pipelineusing Flask; Docker,Jnekins,and Kubernetes (Minikube)


## Project Architecure
* **Application:** Python Flask Microservice
* **Contanerization:** Docker
* ** CI/CD Automation: ** Jenkins
* **orchestration:** Kubernetes locally (minikube)

## Setup Instructions
1. Run `docker build -t flask-app:local .` to test locally
2. Apply kubernetes manifests using `kubectl apply -f ks8/`
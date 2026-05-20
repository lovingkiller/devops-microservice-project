pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                // this step will pull code from GitHub
                checkout scm
            }
        }

        stage('Build Docker Image'){
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t flask-app:local .'
            }
        }

       stage('Deployment to kubernetes') {
            steps {
                echo 'Deploying to Docker Desktop K8s Cluster...'
                // Hum direct token aur server flags dekar config file ko bypass kar rahe hain
                sh '''
                kubectl apply -f k8s/deployment.yaml \
                  --server=https://host.docker.internal:6443 \
                  --insecure-skip-tls-verify=true \
                  --validate=false
                
                kubectl apply -f k8s/service.yaml \
                  --server=https://host.docker.internal:6443 \
                  --insecure-skip-tls-verify=true \
                  --validate=false
                '''
            }
        }
        
        }
    }

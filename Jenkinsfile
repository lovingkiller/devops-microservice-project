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
                sh 'kubectl apply -f k8s/deployment.yaml --validate=false --insecure-skip-tls-verify'
                sh 'kubectl apply -f k8s/service.yaml --validate=false --insecure-skip-tls-verify'
            }
        }
            }
        }
        
        
    

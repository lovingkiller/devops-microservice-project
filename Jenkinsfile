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
                echo 'Deploying to Minikube Clister...'
                sh 'kubectl apply -f k8s/deployment.yaml --validate=false'
                sh 'kubectl apply -f k8s/service.yaml --validate=false'
                sh 'kubectl rollout restart deployment flask-app-deployment'
            }
        }
    }
}
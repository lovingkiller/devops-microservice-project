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
                echo 'Deploying to Minikube Cluster...'
                // `--server` flag laga kar hum kubectl ka muh zabardasti Minikube ki taraf mod rahe hain
                // XXXXX ko apne kubectl cluster-info waale port se badal lena
                sh 'kubectl apply -f k8s/deployment.yaml --server=https://host.docker.internal:XXXXX --validate=false --insecure-skip-tls-verify'
                sh 'kubectl apply -f k8s/service.yaml --server=https://host.docker.internal:XXXXX --validate=false --insecure-skip-tls-verify'
            }
        
        }
    }
}
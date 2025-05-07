pipeline {
    agent any

    environment {
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/RajlaxmiManepatil/Username-password.git'
            }
        }

        

        stage('Build Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Start Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Verify App') {
            steps {
                sh 'curl -s http://localhost:5000'
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
    }
}

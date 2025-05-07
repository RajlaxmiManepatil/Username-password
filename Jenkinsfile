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
                bat 'docker-compose build'
            }
        }

        stage('Start Containers') {
            steps {
                bat 'docker-compose up -d'
                // Optional: wait a bit to let containers start
                bat 'timeout /t 10'
            }
        }

        stage('Verify App') {
            steps {
                script {
                    def response = bat(
                        script: 'curl -s -o nul -w "%%{http_code}" http://localhost:5000',
                        returnStdout: true
                    ).trim()
                    
                    if (response != '200') {
                        error("App did not return 200 OK. Got response code: ${response}")
                    } else {
                        echo "App is running with HTTP ${response}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Build finished. Stopping containers...'
            bat 'docker-compose down'
        }
    }
}

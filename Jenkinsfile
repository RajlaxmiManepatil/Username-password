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
        sleep time: 10, unit: 'SECONDS'
    }
}

      stage('Verify App') {
    steps {
        script {
            def raw = bat(script: 'curl -s -o nul -w "%%{http_code}" http://localhost:5000', returnStdout: true)
            def response = raw.readLines().last().trim()
            echo "HTTP Response Code: ${response}"
            if (response != '200') {
                error "App did not return 200 OK. Got response code: ${response}"
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

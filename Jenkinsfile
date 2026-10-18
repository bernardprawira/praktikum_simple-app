pipeline {
    agent any

    environment {
        IMAGE_NAME = 'bernardprawira/praktikum_simple-app'
        DOCKER_BIN = 'C:/Program Files/Docker/Docker/resources/bin/docker.exe'
    } 
    
    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Melakukan checkout dari SCM...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Membangun Docker Image dari Dockerfile Python...'
                bat "\"${env.DOCKER_BIN}\" build -t ${env.IMAGE_NAME}:${env.BUILD_NUMBER} ."
                bat "\"${env.DOCKER_BIN}\" tag ${env.IMAGE_NAME}:${env.BUILD_NUMBER} ${env.IMAGE_NAME}:latest"
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Mengirim Docker image ke Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat "\"${env.DOCKER_BIN}\" login -u %USER% -p %PASS%"
                    bat "\"${env.DOCKER_BIN}\" push ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                    bat "\"${env.DOCKER_BIN}\" push ${env.IMAGE_NAME}:latest"
                }
            }
        }
    }

    post {
        always {
            echo 'Selesai build & push proyek Python Database 🏁'
        }
    }
}

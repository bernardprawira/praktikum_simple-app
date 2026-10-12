pipeline {
  agent any
  environment {
    IMAGE_NAME = 'bernardprawira/praktikum_simple-app'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') { 
      steps { checkout scm } 
    }
    stage('Build & Test App') { 
      steps { 
        sh 'echo "Menjalankan build aplikasi dan koneksi database..."' 
      } 
    }
    stage('Build Docker Image') {
      steps { 
        sh "docker build -t ${env.IMAGE_NAME}:${env.BUILD_NUMBER} ."
      }
    }
    stage('Push ke Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials',
            usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh "echo $PASS | docker login -u $USER --password-stdin"
          sh "docker push ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
          sh "docker tag ${env.IMAGE_NAME}:${env.BUILD_NUMBER} ${env.IMAGE_NAME}:latest"
          sh "docker push ${env.IMAGE_NAME}:latest"
        }
      }
    }
  }
  post { 
    always { 
      echo 'Pipeline Selesai!' 
    } 
  }
}

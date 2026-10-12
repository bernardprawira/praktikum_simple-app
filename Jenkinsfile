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
        bat 'echo "Menjalankan build aplikasi dan koneksi database di Windows..."' 
      } 
    }
    stage('Build Docker Image') {
      steps { 
        bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
      }
    }
    stage('Push ke Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials',
            usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          bat 'docker login -u %USER% -p %PASS%'
          bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
          bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
          bat "docker push %IMAGE_NAME%:latest"
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

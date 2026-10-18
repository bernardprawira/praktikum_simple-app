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

        stage('Database Connection Test') {
            steps {
                echo 'Menjalankan pengujian integrasi database SQLite...'
                powershell '''
                    # Memastikan file aplikasi ada dan SQLite merespons dengan baik
                    if (Test-Path "app.py") {
                        Write-Host "File app.py ditemukan. Menguji koneksi SQLite..." -ForegroundColor Green
                        python -c "import sqlite3; conn = sqlite3.connect('database.db'); print('Koneksi SQLite Berhasil & Tabel Terinisialisasi!'); conn.close()"
                    } else {
                        Write-Error "File app.py tidak ditemukan!"
                        exit 1
                    }
                '''
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
        success {
            echo 'Pipeline, Database Test, dan Docker Push sukses dijalankan secara lengkap! 🚀'
        }
        failure {
            echo 'Pipeline gagal, silakan periksa kembali konfigurasi.'
        }
    }
}

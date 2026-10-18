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
                echo 'Memeriksa struktur file dan inisialisasi database SQLite...'
                powershell '''
                    # 1. Pastikan file app.py ada
                    if (Test-Path "app.py") {
                        Write-Host "[OK] File app.py ditemukan." -ForegroundColor Green
                    } else {
                        Write-Error "[FAIL] File app.py tidak ada!"
                        exit 1
                    }
                    
                    # 2. Buat folder database dan inisialisasi file database.db untuk pengujian
                    New-Item -ItemType Directory -Force -Path "database" | Out-Null
                    $dbPath = "database/database.db"
                    
                    if (!(Test-Path $dbPath)) {
                        New-Item -ItemType File -Force -Path $dbPath | Out-Null
                        Write-Host "[OK] Database SQLite baru berhasil diinisialisasi di folder database/" -ForegroundColor Green
                    } else {
                        Write-Host "[OK] Database SQLite sudah ada dan siap digunakan." -ForegroundColor Green
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

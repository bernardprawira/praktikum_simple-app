pipeline {
    agent any
    stages {
        stage('Database Connection Test') {
            steps {
                echo 'Menguji koneksi database SQLite...'
                bat '''
                    python -c "import os, sqlite3; os.makedirs('database', exist_ok=True); conn = sqlite3.connect('database/database.db'); print('Koneksi SQLite Berhasil!'); conn.close()"
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Membuat Docker image aplikasi...'
                bat 'docker build -t bernardprawira/praktikum_simple-app:latest .'
            }
        }
        stage('Push ke Docker Hub') {
            steps {
                echo 'Mengirim image ke Docker Hub...'
                bat 'docker push bernardprawira/praktikum_simple-app:latest'
            }
        }
    }
    post {
        success {
            echo 'Pipeline dan pengujian database sukses dijalankan!'
        }
        failure {
            echo 'Pipeline gagal, silakan periksa kembali konfigurasi.'
        }
    }
}

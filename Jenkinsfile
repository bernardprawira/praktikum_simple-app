pipeline {
    agent any
    stages {
        stage('Database Connection Test') {
            steps {
                echo 'Menguji koneksi database SQLite di dalam proyek...'
                bat 'python -c "import sqlite3; conn = sqlite3.connect(\'database/database.db\'); print(\'Koneksi SQLite Berhasil!\'); conn.close()"'
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

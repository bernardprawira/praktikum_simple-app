import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def init_db():
    # Menyimulasikan pembuatan dan koneksi ke database SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS status_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesan TEXT NOT NULL
        )
    ''')
    cursor.execute("INSERT INTO status_log (pesan) VALUES ('Koneksi Database Berhasil!')")
    conn.commit()
    conn.close()
    return "Database SQLite Connected & Initialized!"

@app.route('/')
def hello():
    # Jalankan fungsi inisialisasi database saat route diakses
    db_status = init_db()
    return jsonify({
        "message": "Halo dari Flask + Docker + Jenkins!",
        "database_status": db_status,
        "status": "Success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

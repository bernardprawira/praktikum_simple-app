import os
import sqlite3
from flask import Flask

app = Flask(__name__)

def init_db():
    # Membuat folder 'database' otomatis jika belum ada
    if not os.path.exists('database'):
        os.makedirs('database')
    
    # Membuat koneksi ke file database di dalam folder database/
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kunjungan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def hello():
    init_db()
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO kunjungan DEFAULT VALUES')
    conn.commit()
    cursor.execute('SELECT COUNT(*) FROM kunjungan')
    count = cursor.fetchone()[0]
    conn.close()

    return f"Halo dari Flask + Docker + Jenkins! | Total Kunjungan ke DB: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

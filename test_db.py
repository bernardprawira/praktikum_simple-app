import os
import sqlite3

# Memastikan folder 'database' dibuat jika belum ada
os.makedirs('database', exist_ok=True)

# Membuka koneksi ke database SQLite
conn = sqlite3.connect('database/database.db')
print('Koneksi SQLite Berhasil!')
conn.close()

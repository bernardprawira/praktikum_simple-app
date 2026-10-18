# Gunakan image base Python
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Copy requirements.txt dan install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code project ke container
COPY . .

# Expose port aplikasi (misal Flask/FastAPI)
EXPOSE 5000

# Jalankan aplikasi utama
CMD ["python", "app.py"]

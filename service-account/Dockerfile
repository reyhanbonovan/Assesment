# Gunakan image dasar Python
FROM python:3.10-slim

# Setel direktori kerja
WORKDIR /app

# Salin file requirements.txt dan instal dependensi
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi ke dalam container
COPY . .

# Expose port aplikasi
EXPOSE 8080

# Jalankan aplikasi saat container dimulai
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

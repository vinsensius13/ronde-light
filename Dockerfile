# Gunakan Python base image
FROM python:3.11-slim-bookworm

# Set working directory
WORKDIR /app

# Copy semua file
COPY . .

# Update system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install dependensi
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Jalankan aplikasi
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

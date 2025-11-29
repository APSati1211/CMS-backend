# Step 1: Base image
FROM python:3.12-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install OS dependencies (optional for psycopg2, pillow, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the backend code
COPY . .

# Step 6: Expose backend port (change if yours is different)
EXPOSE 8000

# Step 7: Run Django server (gunicorn recommended)
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]

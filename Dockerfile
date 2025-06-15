# 1. Use base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy all app files
COPY ./api ./api
COPY ./models ./models
COPY ./frontend ./frontend
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose FastAPI port
EXPOSE 8000

# 6. Run the app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]


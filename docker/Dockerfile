FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY utils.py .
COPY trained_model.pkl .

# Environment variables
ENV PORT=8080
ENV MODEL_PATH=/app/trained_model.pkl

# Expose port
EXPOSE 8080

# Health check (Streamlit)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/_stcore/health || exit 1

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

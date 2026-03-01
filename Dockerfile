FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Install build-essential for g++ and Streamlit for the web app
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install --no-cache-dir streamlit \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# (Optional) Create a non-root user for better security
# RUN useradd -m appuser
# Tạo user và cấp quyền ghi cho /workspace
# RUN useradd -m appuser && chown -R appuser /workspace
# USER appuser

# Expose port for Streamlit
EXPOSE 8501

# Copy the Streamlit app into the image
COPY file_manager.py .

# Default command runs Streamlit app
CMD ["streamlit", "run", "file_manager.py", "--server.address=0.0.0.0"]
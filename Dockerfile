FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Install build-essential for g++ and Streamlit for the web app
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install --no-cache-dir streamlit \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 🔥 Fix permission cho OpenShift
RUN chgrp -R 0 /workspace && \
    chmod -R g+rwX /workspace

EXPOSE 8501

# Copy the Streamlit app into the image
COPY file_manager.py .

# Default command runs Streamlit app
CMD ["streamlit", "run", "file_manager.py", "--server.address=0.0.0.0"]
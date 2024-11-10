# Use a Python 3.12 slim as a base image
FROM python:3.12-slim

# Metadata as best practice
LABEL maintainer="devops-team@example.com>"
LABEL description="Dockerfile for a file storage server application using FastAPI"

# Build arguments to pass UID, GID, and username
ARG USER_NAME=fs-user
ARG USER_ID=1000
ARG GROUP_ID=1000

# Set up environment variables
ENV APP_HOME=/app

# Set up working directory
WORKDIR $APP_HOME

# Install necessary system packages for building dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a new group and user with specific UID and GID
RUN groupadd -g $GROUP_ID $USER_NAME && \
    useradd -m -u $USER_ID -g $GROUP_ID -s /bin/bash $USER_NAME

# Copy and install Python dependencies separately to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container and change ownership
COPY . $APP_HOME
RUN chown -R $USER_NAME:$USER_NAME $APP_HOME

# Switch to the non-root user
USER $USER_NAME

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI server as the non-root user
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

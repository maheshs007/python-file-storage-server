# File Storage Server and CLI in Python
A simple File Storage Server with CLI

This project provides a simple file storage server written in Python with a command-line interface (CLI) for uploading, listing, and deleting files.

# Build and Run the server locally, please follow below procedure.
## Installation

### Run with Docker
1. Build the container image:
   ```bash
   docker build -t file-storage-server .
   ```

2. Run the container for file-storage-server:
   ```bash
   docker run -d -p 8000:8000 file-storage-server
   ```

### Install CLI Locally
1. Install the CLI tool:
   ```bash
   pip install -e .
   ```

## Usage

Once the CLI is installed, use it to interact with the server:
We can use `fs-store` command to do file operations.

- **Upload a file**:
  ```bash
  fs-store upload-file /path/to/yourfile.txt
  ```

- **List files**:
  ```bash
  fs-store list-files
  ```

- **Delete a file**:
  ```bash
  fs-store delete-file yourfile.txt
  ```

## Testing

Run unit tests with:
```bash
pytest
```


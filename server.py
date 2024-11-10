# Import necessary libraries from FastAPI and Python's os module
from fastapi import FastAPI, UploadFile, File, HTTPException
import os

# Create an instance of the FastAPI application
app = FastAPI()

# Define the directory where uploaded files will be stored
UPLOAD_FOLDER = "./uploaded_files/"

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Endpoint to upload a file
@app.post("/files/{name}")
async def upload_file(name: str, file: UploadFile = File(...)):
    """
    Uploads a file to the server and saves it in the specified upload folder.
    
    Parameters:
    - name (str): The name under which the file should be saved.
    - file (UploadFile): The file to be uploaded, passed as a form-data.

    Returns:
    - A JSON message confirming successful upload.
    """
    # Generate the complete path for saving the file
    file_path = os.path.join(UPLOAD_FOLDER, name)

    # Write the uploaded file's content to the server storage
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())  # Read file content asynchronously and write to the specified path

    # Return a success message after the file is saved
    return {"message": f"{name} uploaded successfully."}

# Endpoint to delete a specified file
@app.delete("/files/{name}")
async def delete_file(name: str):
    """
    Deletes a file from the server storage if it exists.
    
    Parameters:
    - name (str): The name of the file to delete.

    Returns:
    - A JSON message confirming successful deletion.
    - If the file does not exist, raises an HTTP 404 error.
    """
    # Generate the file path of the file to delete
    file_path = os.path.join(UPLOAD_FOLDER, name)

    # Check if the file exists
    if os.path.exists(file_path):
        # Delete the file if it exists
        os.remove(file_path)
        return {"message": f"{name} deleted successfully."}
    else:
        # Raise an HTTP 404 error if the file does not exist
        raise HTTPException(status_code=404, detail="File not found")

# Endpoint to list all uploaded files
@app.get("/files")
async def list_files():
    """
    Lists all files currently stored in the upload folder.
    
    Returns:
    - A JSON array containing the names of all uploaded files.
    """
    # List all files in the upload directory
    files = os.listdir(UPLOAD_FOLDER)
    return files

import requests
from cli import upload_file
from unittest.mock import patch

def test_upload_file():
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "File uploaded successfully"}

        response = upload_file("/path/to/testfile.txt")
        assert response == {"message": "File uploaded successfully"}
        mock_post.assert_called_once_with(
            "http://localhost:8000/files/testfile.txt",
            files={"file": open("/path/to/testfile.txt", 'rb')}
        )

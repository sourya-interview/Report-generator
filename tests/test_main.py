from fastapi.testclient import TestClient
from app.server import app
import sys, os

client = TestClient(app)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
API_KEY = "supersecret123"

def test_generate_report_success():
    response = client.get("/generate-report/", headers={"x-api-key": API_KEY})
    assert response.status_code == 200
    assert response.json()["message"] == "Report generated successfully"

def test_upload_files_success():
    with open("app/sample_input/input.csv", "rb") as input_file, open("app/sample_input/reference.csv", "rb") as ref_file:
        response = client.post(
            "/upload/",
            headers={"x-api-key": API_KEY},
            files={
                "input_file": ("input.csv", input_file, "text/csv"),
                "reference_file": ("reference.csv", ref_file, "text/csv")
            }
        )
    assert response.status_code == 200
    assert response.json()["message"] == "Files uploaded successfully"

def test_download_report_success():
    response = client.get("/download-report/", headers={"x-api-key": API_KEY})
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]

def test_unauthorized_access():
    response = client.get("/generate-report/")  # no x-api-key
    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"

def test_wrong_api_key():
    response = client.get("/generate-report/", headers={"x-api-key": "wrongkey"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"


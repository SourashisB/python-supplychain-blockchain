from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_good():
    response = client.post("/goods/", json={"name": "Test Good"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Good"

def test_track_good():
    response = client.get("/tracking/1")
    assert response.status_code == 200
    assert "id" in response.json()
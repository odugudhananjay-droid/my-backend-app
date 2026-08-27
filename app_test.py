from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Website Health Checker is running"
    }


def test_check_website_up():
    response = client.get("/check", params={"url": "https://www.google.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "UP"
    assert data["status_code"] == 200


def test_check_website_down():
    response = client.get("/check", params={"url": "https://thisdoesnotexist12345.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "DOWN"
    assert data["status_code"] is None


def test_kesava():
    response = client.get("/kesava")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Kesava is running"
    }
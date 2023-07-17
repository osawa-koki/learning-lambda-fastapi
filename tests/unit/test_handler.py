from fastapi.testclient import TestClient
from src.app import app

testClient = TestClient(app)

def test_get():
    response = testClient.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello GET."}

def test_post():
    response = testClient.post("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello POST."}

def test_put():
    response = testClient.put("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello PUT."}

def test_delete():
    response = testClient.delete("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello DELETE."}

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app

def test_dashboard_route(client):
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'<title>Dashboard</title>' in response.data

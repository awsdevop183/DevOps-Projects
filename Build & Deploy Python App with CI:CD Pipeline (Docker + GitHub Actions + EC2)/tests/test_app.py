import pytest
from app.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ===========================================
# Health Check Tests
# ===========================================

def test_health_returns_200(client):
    response = client.get('/health')
    assert response.status_code == 200


def test_health_returns_healthy(client):
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == 'healthy'


# ===========================================
# Home Endpoint Tests  
# ===========================================

def test_home_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_home_returns_welcome_message(client):
    response = client.get('/')
    data = response.get_json()
    assert 'message' in data


# ===========================================
# Tasks CRUD Tests
# ===========================================

def test_get_tasks_returns_200(client):
    response = client.get('/tasks')
    assert response.status_code == 200


def test_create_task(client):
    response = client.post('/tasks', 
        json={'title': 'Test Task'},
        content_type='application/json'
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test Task'
    assert 'id' in data


def test_create_task_without_title_fails(client):
    response = client.post('/tasks',
        json={'completed': True},
        content_type='application/json'
    )
    assert response.status_code == 400


def test_get_nonexistent_task_returns_404(client):
    response = client.get('/tasks/99999')
    assert response.status_code == 404


def test_delete_task(client):
    # Create a task first
    create_response = client.post('/tasks',
        json={'title': 'Task to delete'},
        content_type='application/json'
    )
    task_id = create_response.get_json()['id']
    
    # Delete it
    delete_response = client.delete(f'/tasks/{task_id}')
    assert delete_response.status_code == 200

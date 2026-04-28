import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Teste 1: Verifica se a rota principal retorna status 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_data(client):
    """Teste 2: Verifica se o conteúdo JSON da home está correto"""
    response = client.get('/')
    data = response.get_json()
    assert data['projeto'] == "Atividade Somativa 1"
    assert data['tecnologia'] == "Python + Flask"

def test_health_status_code(client):
    """Teste 3: Verifica se a rota /health retorna status 200"""
    response = client.get('/health')
    assert response.status_code == 200

def test_health_data(client):
    """Teste 4: Verifica se o status retornado em /health é 'healthy'"""
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == "healthy"

def test_invalid_route(client):
    """Teste 5: Verifica se uma rota inexistente retorna 404"""
    response = client.get('/rota-inexistente')
    assert response.status_code == 404

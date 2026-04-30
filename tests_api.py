import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import numpy as np

# Mock model loading before importing app
with patch('joblib.load') as mock_joblib:
    mock_model = MagicMock()
    mock_model.predict.return_value = np.array([45000.0])
    
    mock_vectorizer = MagicMock()
    mock_vectorizer.transform.return_value = MagicMock()
    mock_vectorizer.transform.return_value.toarray.return_value = np.array([[0.1, 0.2]])
    
    mock_joblib.side_effect = [mock_model, mock_vectorizer]
    
    from api.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["model_loaded"] is True

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "AfriSalaries API" in response.json()["message"]

@patch('shap.TreeExplainer')
def test_predict_endpoint_success(mock_shap):
    mock_explainer = MagicMock()
    mock_explainer.shap_values.return_value = np.array([[0.2, 0.1, 0.05]])
    mock_shap.return_value = mock_explainer
    
    payload = {
        "description": "Senior Python Developer with 5+ years Django, AWS. Remote. Nairobi.",
        "country": "KE",
        "currency": "USD"
    }
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "salary_low" in data
    assert "salary_mid" in data
    assert "salary_high" in data
    assert data["currency"] == "USD"
    assert 0 <= data["confidence"] <= 1
    assert isinstance(data["top_factors"], list)

def test_predict_validation_error():
    payload = {"description": "short", "country": "KE"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422

def test_predict_invalid_country():
    payload = {
        "description": "Senior Python Developer with 5+ years Django, AWS. Remote. Nairobi.",
        "country": "USA",
        "currency": "USD"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422

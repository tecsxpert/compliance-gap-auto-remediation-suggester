import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


# ------------------------------
# 1. Test /describe success
# ------------------------------
def test_describe_success(client):
    response = client.post("/describe", json={
        "standard": "ISO 27001",
        "department": "IT",
        "control_area": "Access Control",
        "current_situation": "Weak password policy",
        "expected_requirement": "Strong password policy required",
        "risk_level": "High"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert "gap_title" in data


# ------------------------------
# 2. Test /recommend success
# ------------------------------
def test_recommend_success(client):
    response = client.post("/recommend", json={
        "standard": "ISO 27001",
        "department": "IT",
        "control_area": "Access Control",
        "current_situation": "Weak password policy",
        "expected_requirement": "Strong password policy required",
        "risk_level": "High"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert "recommendations" in data


# ------------------------------
# 3. Test /generate-report success
# ------------------------------
def test_report_success(client):
    response = client.post("/generate-report", json={
        "standard": "ISO 27001",
        "department": "IT",
        "control_area": "Access Control",
        "current_situation": "Weak password policy",
        "expected_requirement": "Strong password policy required",
        "risk_level": "High"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert "title" in data


# ------------------------------
# 4. Missing field test
# ------------------------------
def test_missing_field(client):
    response = client.post("/describe", json={})
    assert response.status_code == 400


# ------------------------------
# 5. Malicious input test
# ------------------------------
def test_malicious_input(client):
    response = client.post("/describe", json={
        "standard": "<script>alert(1)</script>",
        "department": "IT",
        "control_area": "Access Control",
        "current_situation": "Weak password policy",
        "expected_requirement": "Strong password policy required",
        "risk_level": "High"
    })

    assert response.status_code == 400


# ------------------------------
# 6. Health endpoint test
# ------------------------------
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200


# ------------------------------
# 7. Invalid route test
# ------------------------------
def test_invalid_route(client):
    response = client.get("/invalid")
    assert response.status_code == 404


# ------------------------------
# 8. Empty string input test
# ------------------------------
def test_empty_input(client):
    response = client.post("/describe", json={
        "standard": "",
        "department": "",
        "control_area": "",
        "current_situation": "",
        "expected_requirement": "",
        "risk_level": ""
    })

    assert response.status_code == 400
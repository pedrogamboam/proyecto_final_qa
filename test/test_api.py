import requests
from utils.logger import logger
import pytest_check as check
import pytest



headers = {
        "x-api-key" : "reqres_eb2b8a5025d3430398fdf8cc2f2f8e05"
    }

@pytest.mark.api
def test_login_valido():
    body = {
        "email" : "eve.holt@reqres.in",
        "password" : "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 200

@pytest.mark.api
def test_login_sin_password():
    body = {
        "email" : "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 400

@pytest.mark.api
def test_create_user():
    body = {
        "name": "Jose",
        "email": "jose.montezuma@bue.edu.ar",
        "password": "12345"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

    data = response.json()

    assert response.status_code == 201
    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 204


def test_get_user():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 200
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion tardo mas de lo esperado"

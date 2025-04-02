import requests
import pytest


class EmployeeApi:
    def __init__(self, base_url="http://5.101.50.27:8000"):
        self.base_url = base_url

    def create_employee(self, data):
        url = f"{self.base_url}/employee/create"
        return requests.post(url, json=data)

    def get_employee_info(self, employee_id):
        url = f"{self.base_url}/employee/info"
        params = {"id": employee_id}
        return requests.get(url, params=params)

    def update_employee(self, employee_id, changes):
        url = f"{self.base_url}/employee/change"
        data = {"id": employee_id, **changes}
        return requests.patch(url, json=data)


class TestEmployeeApi:
    @pytest.fixture
    def api(self):
        return EmployeeApi()

    @pytest.fixture
    def valid_employee_data(self):
        return {
            "name": "Иван Иванов",
            "position": "Разработчик",
            "department": "IT",
            "salary": 100000,
            "email": "ivanov@example.com",
            "hire_date": "2023-01-01"
        }

    @pytest.fixture
    def minimal_employee_data(self):
        return {
            "name": "Минимальный Тест",
            "position": "Тестовая должность"
        }

    def test_create_employee_success(self, api, valid_employee_data):
        response = api.create_employee(valid_employee_data)
        assert response.status_code == 201
        employee_data = response.json()
        assert "id" in employee_data
        return employee_data["id"]

    def test_create_employee_minimal(self, api, minimal_employee_data):
        response = api.create_employee(minimal_employee_data)
        assert response.status_code == 201

    def test_get_employee_info(self, api, valid_employee_data):
        employee_id = self.test_create_employee_success(api, valid_employee_data)
        response = api.get_employee_info(employee_id)
        assert response.status_code == 200
        employee_info = response.json()
        assert employee_info["id"] == employee_id
        assert employee_info["name"] == valid_employee_data["name"]
        assert employee_info["position"] == valid_employee_data["position"]

    def test_update_employee(self, api, valid_employee_data):
        employee_id = self.test_create_employee_success(api, valid_employee_data)
        updates = {"position": "Старший разработчик", "salary": 120000}
        response = api.update_employee(employee_id, updates)
        assert response.status_code == 200
        updated_info = api.get_employee_info(employee_id).json()
        assert updated_info["position"] == updates["position"]
        assert updated_info["salary"] == updates["salary"]

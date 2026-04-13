import unittest
import json
from backend.app import app

# filepath: /home/camper/Escritorio/Actividad/control_pc/backend/test_app.py

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_file = "data.json"

        # Ensure the data file is empty before each test
        with open(self.data_file, "w") as f:
            json.dump([], f)

    def tearDown(self):
        # Clean up after tests
        with open(self.data_file, "w") as f:
            json.dump([], f)

    def test_post_registro_valid(self):
        """Test POST /registro with valid data"""
        payload = {
            "pc": "test-pc",
            "usuarios": "test-user",
            "uptime": "up 1 hour",
            "timestamp": "2026-04-13T10:00:00"
        }
        response = self.app.post("/registro", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Registro guardado", response.get_json()["mensaje"])

        # Verify the data was saved
        with open(self.data_file, "r") as f:
            registros = json.load(f)
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0], payload)

    def test_post_registro_invalid(self):
        """Test POST /registro with invalid data"""
        payload = {"pc": "test-pc"}  # Missing required fields
        response = self.app.post("/registro", json=payload)
        self.assertEqual(response.status_code, 500)  # Expecting server error due to missing fields

    def test_get_registros(self):
        """Test GET /registros"""
        # Prepopulate the data file
        registros = [
            {
                "pc": "test-pc",
                "usuarios": "test-user",
                "uptime": "up 1 hour",
                "timestamp": "2026-04-13T10:00:00"
            }
        ]
        with open(self.data_file, "w") as f:
            json.dump(registros, f)

        response = self.app.get("/registros")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), registros)

if __name__ == "__main__":
    unittest.main()
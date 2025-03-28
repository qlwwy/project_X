import unittest
from src.utils import load_transactions
import json
from unittest.mock import patch, mock_open


class TestLoadTransactions(unittest.TestCase):

    def test_file_does_not_exist(self):
        # Тест, когда файл не существует
        with patch("os.path.exists", return_value=False):
            result = load_transactions("nonexistent_file.json")
            self.assertEqual(result, [])

    def test_file_contains_valid_json_list(self):
        # Тест, когда файл содержит корректные данные в формате JSON
        valid_json = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
        with patch("os.path.exists", return_value=True):
            with patch("os.path.getsize", return_value=len(valid_json)):
                with patch("builtins.open", mock_open(read_data=valid_json)):
                    result = load_transactions("valid_file.json")
                    self.assertEqual(result, json.loads(valid_json))

    def test_file_contains_invalid_json(self):
        # Тест, когда файл содержит некорректные данные (не JSON)
        invalid_json = "invalid json data"
        with patch("os.path.exists", return_value=True):
            with patch("os.path.getsize", return_value=len(invalid_json)):
                with patch("builtins.open", mock_open(read_data=invalid_json)):
                    result = load_transactions("invalid_file.json")
                    self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()

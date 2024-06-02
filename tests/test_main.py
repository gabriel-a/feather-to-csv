import unittest
import os
from io import StringIO
import sys
import contextlib
import pandas as pd
from main import main as main_script
import json


class TestMainScript(unittest.TestCase):

    def setUp(self):
        # Create sample JSON and Feather files
        self.json_file = 'test.json'
        self.feather_file = 'test.feather'
        self.csv_file = 'test.csv'
        data = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['A', 'B', 'C']
        })
        json_data = {
            'metadata': {
                'info': 'sample data'
            },
            'data': [
                {'col1': 1, 'col2': 'A'},
                {'col1': 2, 'col2': 'B'},
                {'col1': 3, 'col2': 'C'}
            ]
        }
        with open(self.json_file, 'w') as f:
            json.dump(json_data, f)
        data.to_feather(self.feather_file)

    def tearDown(self):
        # Remove the test files after tests
        for file in [self.json_file, self.feather_file, self.csv_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_json_conversion(self):
        # Capture the output
        captured_output = StringIO()
        sys.argv = ['main.py', self.json_file, self.csv_file]
        with contextlib.redirect_stdout(captured_output):
            main_script()

        self.assertTrue(os.path.exists(self.csv_file))
        self.assertIn(f"CSV file created successfully at: {self.csv_file}", captured_output.getvalue().strip())

        # Check the content of the CSV file
        data = pd.read_csv(self.csv_file)
        self.assertEqual(len(data), 3)
        self.assertEqual(list(data.columns), ['col1', 'col2'])
        self.assertEqual(data['col1'].tolist(), [1, 2, 3])
        self.assertEqual(data['col2'].tolist(), ['A', 'B', 'C'])

    def test_feather_conversion(self):
        # Capture the output
        captured_output = StringIO()
        sys.argv = ['main.py', self.feather_file, self.csv_file]
        with contextlib.redirect_stdout(captured_output):
            main_script()

        self.assertTrue(os.path.exists(self.csv_file))
        self.assertIn(f"CSV file created successfully at: {self.csv_file}", captured_output.getvalue().strip())

        # Check the content of the CSV file
        data = pd.read_csv(self.csv_file)
        self.assertEqual(len(data), 3)
        self.assertEqual(list(data.columns), ['col1', 'col2'])
        self.assertEqual(data['col1'].tolist(), [1, 2, 3])
        self.assertEqual(data['col2'].tolist(), ['A', 'B', 'C'])


if __name__ == '__main__':
    unittest.main()

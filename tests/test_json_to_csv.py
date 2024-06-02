import unittest
import pandas as pd
import os
from json_to_csv import convert_json_to_csv
from io import StringIO
import sys
import contextlib
import json


class TestJsonToCsvConversion(unittest.TestCase):

    def setUp(self):
        # Create a sample JSON file with a list
        self.json_file = 'test.json'
        self.csv_file = 'test.csv'
        data = {
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
            json.dump(data, f)

    def tearDown(self):
        # Remove the test files after tests
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_conversion(self):
        # Capture the output
        captured_output = StringIO()
        with contextlib.redirect_stdout(captured_output):
            # Test the conversion function
            result = convert_json_to_csv(self.json_file, self.csv_file)

        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.csv_file))
        self.assertIn(f"CSV file created successfully at: {self.csv_file}", captured_output.getvalue().strip())

        # Check the content of the CSV file
        data = pd.read_csv(self.csv_file)
        self.assertEqual(len(data), 3)
        self.assertEqual(list(data.columns), ['col1', 'col2'])
        self.assertEqual(data['col1'].tolist(), [1, 2, 3])
        self.assertEqual(data['col2'].tolist(), ['A', 'B', 'C'])

    def test_invalid_input_file(self):
        # Capture the output
        captured_output = StringIO()
        with contextlib.redirect_stdout(captured_output):
            # Test with an invalid input file
            result = convert_json_to_csv('invalid.json', self.csv_file)

        self.assertFalse(result)
        self.assertIn("Error:", captured_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()

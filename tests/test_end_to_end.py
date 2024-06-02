import unittest
import os
import pandas as pd
import json
from main import main as main_script
from io import StringIO
import contextlib
import sys
from datetime import datetime


class TestEndToEnd(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_files'
        self.result_dir = os.path.join(self.test_dir, 'results')
        os.makedirs(self.result_dir, exist_ok=True)

    def generate_unique_filename(self, base_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{base_name}_{timestamp}.csv"

    def test_convert_files(self):
        # Find all JSON and Feather files in the test directory
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            if filename.endswith('.json') or filename.endswith('.feather'):
                # Determine the output CSV file path with a unique timestamp
                csv_filename = self.generate_unique_filename(os.path.splitext(filename)[0])
                csv_file_path = os.path.join(self.result_dir, csv_filename)

                # Capture the output
                captured_output = StringIO()
                sys.argv = ['main.py', file_path, csv_file_path]
                with contextlib.redirect_stdout(captured_output):
                    main_script()

                # Verify the CSV file is created
                self.assertTrue(os.path.exists(csv_file_path), f"CSV file was not created for {file_path}")
                self.assertIn(f"CSV file created successfully at: {csv_file_path}", captured_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()

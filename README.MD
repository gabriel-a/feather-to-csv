# JSON and Feather to CSV Converter

This application converts JSON and Feather files to CSV format. It includes an end-to-end test suite to verify the conversion process.

## Directory Structure

```
your_project_directory/
├── main.py
├── json_to_csv.py
├── feather_to_csv.py
├── requirements.txt
├── test_files/
│ ├── test.json
│ ├── test.feather
│ └── results/
├── .gitignore
└── tests/
└── test_end_to_end.py
```

## Requirements

- Python 3.6 or higher
- Pandas
- PyArrow

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Conversion Script

To convert a JSON or Feather file to CSV, use the `main.py` script. The script automatically detects the file type based on the extension and performs the conversion.

```sh
python main.py <input_file> <output_file>
```

### To run tests
```
python -m unittest discover -s tests
```

### Running the End-to-End Tests
The end-to-end tests read JSON and Feather files from the test_files directory, use the main.py script to generate unique timestamped CSV files in the test_files/results directory, verify that the CSV files are created, and retain the results.

### Adding Test Files
Place your JSON and Feather files in the test_files directory.
Running the Tests
```
python -m unittest discover -s tests
```
When you run the end-to-end tests, any JSON or Feather files in the test_files directory will be automatically converted to CSV files in the test_files/results directory with unique timestamped filenames.

### Examples
```
python main.py test_files/test.json test_files/results/output.csv
python main.py test_files/test.feather test_files/results/output.csv
```

### To run feather_to_csv
```
python feather_to_csv.py path_to_your/SOL_USDT-5m.feather path_to_your/SOL_USDT-5m.csv
```

### For windows feather_to_csv
```
python feather_to_csv.py C:/data/SOL_USDT-5m.feather C:/data/SOL_USDT-5m.csv
```

### To run json_to_csv
```
python json_to_csv.py path_to_your/SOL_USDT-5m.json path_to_your/SOL_USDT-5m.csv
```

### For windows json_to_csv
```
python json_to_csv.py C:/data/SOL_USDT-5m.json C:/data/SOL_USDT-5m.csv
```

### Summary

This `README.md` file provides instructions on how to set up and use the JSON and Feather to CSV conversion application, as well as how to run the end-to-end tests. It includes the directory structure, installation steps, usage examples, and details on running tests.

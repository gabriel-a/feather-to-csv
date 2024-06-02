import argparse
import os
from json_to_csv import convert_json_to_csv
from feather_to_csv import convert_feather_to_csv


def main():
    parser = argparse.ArgumentParser(description='Convert JSON or Feather file to CSV')
    parser.add_argument('input_file', type=str, help='Path to the input JSON or Feather file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension == '.json':
        result = convert_json_to_csv(input_file, output_file, print_message=False)
    elif file_extension == '.feather':
        result = convert_feather_to_csv(input_file, output_file, print_message=False)
    else:
        print("Unsupported file type. Please provide a JSON or Feather file.")
        result = False

    if result:
        print(f"CSV file created successfully at: {output_file}")
    else:
        print(f"Failed to create CSV file from: {input_file}")


if __name__ == "__main__":
    main()

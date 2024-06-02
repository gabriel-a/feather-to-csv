import pandas as pd
import argparse
import json


def find_first_list(data):
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        for key, value in data.items():
            result = find_first_list(value)
            if result is not None:
                return result
    return None


def convert_json_to_csv(input_file, output_file, print_message=True):
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)

        first_list = find_first_list(data)

        if first_list is None:
            raise ValueError("No list found in the JSON file.")

        df = pd.DataFrame(first_list)
        df.to_csv(output_file, index=False)
        if print_message:
            print(f"CSV file created successfully at: {output_file}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Convert JSON file to CSV')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')

    args = parser.parse_args()

    convert_json_to_csv(args.input_file, args.output_file, print_message=False)


if __name__ == "__main__":
    main()

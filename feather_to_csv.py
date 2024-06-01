import pandas as pd
import argparse


def convert_feather_to_csv(input_file, output_file):
    try:
        # Load the .feather file
        data = pd.read_feather(input_file)

        # Save the DataFrame to a .csv file
        data.to_csv(output_file, index=False)
        print(f"CSV file created successfully at: {output_file}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Convert Feather file to CSV')
    parser.add_argument('input_file', type=str, help='Path to the input Feather file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')

    args = parser.parse_args()

    convert_feather_to_csv(args.input_file, args.output_file)


if __name__ == "__main__":
    main()

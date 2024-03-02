import csv
import argparse

def write_employee_details_to_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['emp_id', 'emp_name'])  # Write header
            for emp_id, emp_name in data:
                writer.writerow([emp_id, emp_name])
        print(f"Employee details have been written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")

def parse_csv_file(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                emp_id, emp_name = row
                print(f"Employee ID: {emp_id}, Employee Name: {emp_name}")
    except Exception as e:
        print(f"An error occurred while parsing {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse employee details CSV file.')
    parser.add_argument('-f', '--filename', required=True, help='Path to the CSV file')
    args = parser.parse_args()

    parse_csv_file(args.filename)

import csv

def write_employee_details_to_csv(filename, emp_ids, emp_names):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['emp_id', 'emp_name'])  # Write header
            for emp_id, emp_name in zip(emp_ids, emp_names):
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
    # Hardcoded employee IDs and names
    emp_ids = ["01", "02", "03"]
    emp_names = ["sachin", "rahul", "virat"]

    # Filename to write to
    filename = "employees.csv"

    write_employee_details_to_csv(filename, emp_ids, emp_names)
    parse_csv_file(filename)

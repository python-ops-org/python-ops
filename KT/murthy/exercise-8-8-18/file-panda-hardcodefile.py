import pandas as pd

def write_employee_details_to_csv(filename, emp_ids, emp_names):
    try:
        df = pd.DataFrame({'emp_id': emp_ids, 'emp_name': emp_names})
        df.to_csv(filename, index=False)
        print(f"Employee details have been written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")

def parse_csv_file(filename):
    try:
        df = pd.read_csv(filename)
        for index, row in df.iterrows():
            print(f"Employee ID: {row['emp_id']}, Employee Name: {row['emp_name']}")
    except Exception as e:
        print(f"An error occurred while parsing {filename}: {e}")

if __name__ == "__main__":
    # Hardcoded filename
    filename = "employee_details.csv"

    # Hardcoded employee IDs and names
    emp_ids = ["01", "02", "03"]
    emp_names = ["sachin", "rahul", "virat"]

    write_employee_details_to_csv(filename, emp_ids, emp_names)
    parse_csv_file(filename)

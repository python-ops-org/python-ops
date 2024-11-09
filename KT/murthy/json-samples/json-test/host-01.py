import json

# Open and load the JSON file
with open("host-tower.json", "r") as f:
    datax = json.load(f)

# Loop through each host entry in the 'results' list and print the host name
for entry in datax.get("results", []):
    try:
        # Get the host name from the 'name' field
        host_name = entry.get("name", "No name found")
        print(f"{host_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
        continue


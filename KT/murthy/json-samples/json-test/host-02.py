import json

# Open the file and load JSON data
f = open("host-tower.json", "r")
data = json.load(f)

# Initialize a list to store host names
host_names = []

# Use a while loop to handle pagination (assuming next page fetching)
while True:
    # Process each host in the current page's results
    num = len(data["results"])
    for i in range(num):
        # Extract and store the host name
        host_name = data["results"][i]["name"]
        host_names.append(host_name)
    
    # Check if there’s a next page to process
    if data["next"] is None:
        # If no next page, exit the loop
        break
    else:
        # Here, you'd typically fetch the next page and update `data`
        # For example: data = fetch_data_from_url(data["next"])
        # Since we don't have actual pagination, we'll simulate by breaking here.
        break

# Print each host name on a new line
for host in host_names:
    print(host)

# Close the file
f.close()

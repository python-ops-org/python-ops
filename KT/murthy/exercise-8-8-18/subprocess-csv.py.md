
```
import csv
import subprocess

# Open the CSV file
f = open("nodes.csv", newline='', mode='r')
reader = csv.DictReader(f)

# List to store server details
servers = []

for row in reader:
    if 'ip' in row and 'user' in row:
        servers.append({
            'host': row['ip'],
            'user': row['user'],
            'password': row.get('pass', '')  # Handle missing passwords
        })

f.close()

# Commands dictionary
COMMANDS = {
    'memory': "free -m | sed -n '2p' | tr -s ' ' | cut -d' ' -f3",
    'disk': "df -h | grep '/$' | tr -s ' ' | cut -d' ' -f3"
}

def run_ssh_command(server, command):
    """Execute SSH command and return output"""
    if not server['password']:
        return "Error: No password provided"

    ssh_cmd = f"""sshpass -p '{server['password']}' ssh -o StrictHostKeyChecking=no {server['user']}@{server['host']} "{command}" """
    
    try:
        output = subprocess.run(ssh_cmd, shell=True, capture_output=True, text=True)

        if output.returncode == 0:
            return output.stdout.strip()
        else:
            return "Error: " + output.stderr.strip()

    except Exception as e:
        return "Error: " + str(e)

# Print header
print(f"{'Host':<15} {'Memory Usage (MB)':<20} {'Disk Usage':<15}")
print("-" * 50)

# Check each server
for server in servers:
    memory = run_ssh_command(server, COMMANDS['memory'])
    disk = run_ssh_command(server, COMMANDS['disk'])
    
    print(f"{server['host']:<15} {memory:<20} {disk:<15}")



```

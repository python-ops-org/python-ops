
```

import subprocess

# List of servers
servers = [
    {
        "host": "127.0.0.1",
        "user": "xxx",
        "password": "xxxx"
    },
    {
        "host": "192.168.15.654",
        "user": "xxx",
        "password": "xxxx"
    }
]

# Commands dictionary
COMMANDS = {
    'memory': "free -m | sed -n '2p' | tr -s ' ' | cut -d' ' -f3",
    'disk': "df -h | grep '/$' | tr -s ' ' | cut -d' ' -f3"
}

def run_ssh_command(server, command):
    """Execute SSH command and return output"""
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
print(f"{'Host':<20} {'Memory Usage (MB)':<20} {'Disk Usage':<15}")
print("-" * 55)

# Check each server
for server in servers:
    memory = run_ssh_command(server, COMMANDS['memory'])
    disk = run_ssh_command(server, COMMANDS['disk'])

    print(f"{server['host']:<20} {memory:<20} {disk:<15}")


```

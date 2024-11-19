import subprocess

# List of servers
servers = [
    {
        "host": "127.0.0.1",
        "user": "root",
        "password": "iis123"
    },
    {
        "host": "192.168.0.205",
        "user": "root",
        "password": "iis123"
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
        return output.stdout.strip() if output.returncode == 0 else f"Error: {output.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"

# Print header
print(f"{'Host'} {'Memory Usage (MB)'} {'Disk Usage'}")
print("-" * 50)

# Check each server
for server in servers:
    memory = run_ssh_command(server, COMMANDS['memory'])
    disk = run_ssh_command(server, COMMANDS['disk'])
    
    print(f"{server['host']} {memory} {disk}")

import paramiko

def ssh_execute_command(hostname, username, password, command):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()

        # Automatically add host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host using password authentication
        client.connect(hostname, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Read the output
        output = stdout.read().decode("utf-8").strip()  # Strip leading/trailing whitespaces
        error = stderr.read().decode("utf-8").strip()

        # Close the SSH connection
        client.close()

        return output if not error else f"Error: {error}"  # Return output or error message
    except Exception as e:
        return f"Error: {str(e)}"

# List of servers
servers = [
    {
        "ansible_ssh_host": "127.0.0.1",
        "ansible_ssh_user": "xxxx",
        "ansible_ssh_password": "xxxx"
    },
    {
        "ansible_ssh_host": "xxxxx",
        "ansible_ssh_user": "xxxxx",
        "ansible_ssh_password": "xxxxx"
    }
]

# Commands dictionary
COMMANDS = {
    'memory': "free -m | sed -n '2p' | tr -s ' ' | cut -d' ' -f3",
    'disk': "df -h | grep '/$' | tr -s ' ' | cut -d' ' -f3"
}

# Print the header
print(f"{'Host':<15}{'Memory Usage (MB)':<20}{'Disk Usage':<20}")

# Iterate through the servers and fetch memory and disk usage
for server in servers:
    hostname = server["ansible_ssh_host"]
    
    memory_output = ssh_execute_command(
        hostname,
        server["ansible_ssh_user"],
        server["ansible_ssh_password"],
        COMMANDS['memory']
    )
    
    disk_output = ssh_execute_command(
        hostname,
        server["ansible_ssh_user"],
        server["ansible_ssh_password"],
        COMMANDS['disk']
    )

    # Print formatted output
    print(f"{hostname:<15}{memory_output:<20}{disk_output:<20}")

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
        output = stdout.read().decode("utf-8")

        # Close the SSH connection
        client.close()

        return output.strip()  # Strip leading/trailing whitespaces
    except Exception as e:
        return str(e)


# List of servers
servers = [
    {
        "ansible_ssh_host": "127.0.0.1",
        "ansible_ssh_user": "root",
        "ansible_ssh_password": "iis123"
    },
    {
        "ansible_ssh_host": "192.168.0.205",
        "ansible_ssh_user": "root",
        "ansible_ssh_password": "iis123"
    }
]

# Commands to execute
memory_command = "free -m | sed -n '2p' | awk '{print $3;}'"
cpu_command = (
    "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1\"%\"}'"
)

# Print the header
print("Host\t\tMemory_Usage\tCPU_Usage")

# Iterate through the servers and fetch memory and CPU usage
for server in servers:
    memory_output = ssh_execute_command(
        server["ansible_ssh_host"],
        server["ansible_ssh_user"],
        server["ansible_ssh_password"],
        memory_command
    )
    cpu_output = ssh_execute_command(
        server["ansible_ssh_host"],
        server["ansible_ssh_user"],
        server["ansible_ssh_password"],
        cpu_command
    )

    # Use "ansible_ssh_host" as hostname for the output
    hostname = server["ansible_ssh_host"]
    
    # Format the output
    output = f"{hostname}\t{memory_output}\t\t{cpu_output}"

    # Print the output
    print(output)

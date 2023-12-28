import subprocess

def is_port_open(port):
    try:
        # Run netstat command to check if port is open
        result = subprocess.run(['netstat', '-an'], stdout=subprocess.PIPE, text=True)

        # Check if the output contains the port in the listening state
        return f':{port}' in result.stdout and 'LISTEN' in result.stdout
    except Exception as e:
        print(f"Error checking port: {e}")
        return False

# Example usage for port 80
port_to_check = 80
if is_port_open(port_to_check):
    print(f"Port {port_to_check} is open.")
else:
    print(f"Port {port_to_check} is not open.")

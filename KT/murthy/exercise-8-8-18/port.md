
```

import subprocess

def check_port(port):
    try:
        # Execute the netstat command to list listening TCP ports
        output = subprocess.check_output(['netstat', '-ntlp']).decode('utf-8')
        # Split the output by lines and iterate over them
        for line in output.split('\n'):
            # Check if the line contains the port number
            if f':{port}' in line:
                # If the port is found in the line, return True (open)
                return True
        # If the port is not found in any line, return False (closed)
        return False
    except subprocess.CalledProcessError:
        # Handle if the netstat command fails
        print("Error executing netstat command.")
        return False

# Example usage:
p = 80  # Replace with the port number you want to check
if check_port(p):
    print(f"Port {p} is OPEN")
else:
    print(f"Port {p} is CLOSED")
```

```
import socket

def check_port(port, host='127.0.0.1'):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Set timeout so it doesn't hang
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            return result == 0  # 0 means port is open
    except Exception as e:
        print(f"Error checking port {port}: {e}")
        return False

def main():
    port = 80  # Change this as needed
    if check_port(port):
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")

if __name__ == '__main__':
    main()

```











```

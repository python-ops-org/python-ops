import socket

def check_port(host, port=80):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set a timeout for the connection attempt

        # Try connecting to the host on port 80
        result = sock.connect_ex((host, port))

        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} on {host} is open.")
        else:
            print(f"Port {port} on {host} is closed or unreachable.")
    except socket.error as e:
        print(f"Error occurred: {e}")
    finally:
        sock.close()

# Replace 'your_host' with the actual host IP or domain name
check_port('your_host')  # Default port is 80, but you can change it

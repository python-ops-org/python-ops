import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Corrected here
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

# Corrected the port to an integer
check_port('127.0.0.1', 445)

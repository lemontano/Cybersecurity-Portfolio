#Creating a post scanner

#Imports the socket module: This module provides low-level networking interfaces, which are used here to create a socket and check connectivity.

#Prompts the user for an IP address: The user is asked to enter an IP address that they want to scan for open ports.

import socket
import time
import threading

def scan_port(target_ip, port):
    """Scan a single port on the target IP."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout of 1 second
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    target_ip = input("Enter the target IP address: ")
    print("*" * 40)
    print(f"* Scanning: {target_ip} *")
    print("*" * 40)

    threads = []
    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()
        threads.append(thread)

    def timeout_handler():
        print("\nTimeout! Shutting down...")
        for thread in threads:
            thread.join(timeout=0.1)  # Try to join all threads with a short timeout
        exit()

    timer = threading.Timer(300.0, timeout_handler)  # 300 seconds = 5 minutes
    timer.start()

    for thread in threads:
        thread.join()  # Wait for all threads to finish

if __name__ == "__main__":
    main()
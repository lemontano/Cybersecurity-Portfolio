#Creating a post scanner

#Imports the socket module: This module provides low-level networking interfaces, which are used here to create a socket and check connectivity.

#Prompts the user for an IP address: The user is asked to enter an IP address that they want to scan for open ports.

import socket

print("Please enter an IP Address to scan.")
target = input("> ")
print("*" * 40)
print("* Scanning: " + target + " *")
print("*" * 40)

#Prints a header for the scan: This is a visual cue to show the start of the scanning process.

for port in range(1, 1025):
  
#Creates a new socket for each port: A socket is created for each port to attempt a connection.
  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
#Attempts to connect to the target IP and port: The connect_ex method is used here. This method returns 0 if the connection is successful, which means the port is open. Otherwise, it returns an error code.
  
    result = s.connect_ex((target, port))
#Checks the result of the connection attempt: If the result is 0, it prints that the port is open. If not, it does nothing.
  
    if result == 0:
        print("Port: " + str(port) + " Open")
      
#Closes the socket: After checking each port, the socket is closed to free up resources.
    s.close()

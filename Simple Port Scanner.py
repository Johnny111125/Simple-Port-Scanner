import socket

def sniff_ports(host, start_port, end_port, protocol):
  # Initialize a list for open ports
  open_ports = []

  # Iterate through the range of ports
  for port in range(start_port, end_port + 1):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == "tcp" else socket.SOCK_DGRAM)

    # Set a timeout for the socket
    s.settimeout(0.01)

    # Try to connect to the port
    result = s.connect_ex((host, port))

    # If the connection is successful, the port is open
    if result == 0:
      print("\033[92mPort {}/{} is open\033[0m".format(port, protocol))
      open_ports.append(port)
    else:
      print("\033[91mPort {}/{} is closed\033[0m".format(port, protocol))

    # Close the socket
    s.close()

  # Print a summary of the findings
  print("\nScan complete!")
  if open_ports:
    print("\033[92mOpen ports: {}\033[0m".format(", ".join(str(p) for p in open_ports)))
  else:
    print("No open ports found.")
# Prompt the user for a hostname and a protocol
host = input("Enter a hostname to scan: ")
protocol = input("Enter a protocol (tcp or udp): ")

# Sniff the ports on the specified host from 1 to 1024
sniff_ports(host, 1, 1024, protocol)
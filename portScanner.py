import socket
import argparse
from datetime import datetime

# Function to perform TCP port scanning
def scan_tcp_ports(target, start_port, end_port):
    print(f"\nScanning TCP ports on {target} from {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout after 1 second if no response
        result = sock.connect_ex((target, port))  # Connect to the port
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

# Function to perform UDP port scanning (optional, basic implementation)
def scan_udp_ports(target, start_port, end_port):
    print(f"\nScanning UDP ports on {target} from {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

# Main function to parse arguments and call the scanner
if _name_ == "_main_":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP or hostname to scan")
    parser.add_argument("-sp", "--start-port", type=int, help="Starting port for scan", default=1)
    parser.add_argument("-ep", "--end-port", type=int, help="Ending port for scan", default=65535)
    parser.add_argument("-t", "--type", choices=["tcp", "udp"], help="Type of scan: tcp or udp", default="tcp")

    args = parser.parse_args()
    target = args.target
    start_port = args.start_port
    end_port = args.end_port
    scan_type = args.type

    # Print scan information
    print(f"\nStarting {scan_type.upper()} scan on target: {target}")
    print(f"Time started: {str(datetime.now())}")
    
    # Perform the scan based on type
    try:
        if scan_type == "tcp":
            open_ports = scan_tcp_ports(target, start_port, end_port)
        else:
            open_ports = scan_udp_ports(target, start_port, end_port)

        # Print results
        if open_ports:
            print(f"\nOpen {scan_type.upper()} ports on {target}: {open_ports}")
        else:
            print(f"\nNo open {scan_type.upper()} ports found on {target}.")
    
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    
    except socket.gaierror:
        print(f"\nError: Could not resolve hostname {target}.")
    
    except socket.error:
        print("\nError: Could not connect to target.")

    print(f"\nTime finished: {str(datetime.now())}\n")

# For output: python filename.py 192.168.1.1 (ip) --start-port 53 --end-port 123 -- type udp/tcp
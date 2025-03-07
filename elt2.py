# Import necessary modules
import socket
import platform

def get_machine_ip():
    """
    This function retrieves the IP address of the current machine.
    
    Steps:
    1. Get the hostname of the machine using socket.gethostname().
    2. Convert the hostname to an IP address using socket.gethostbyname().
    """
    # Get the hostname
    hostname = socket.gethostname()
    # Get the IP address
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_machine_name():
    """
    This function retrieves the machine name (hostname) using the platform module.
    
    platform.node() returns the machine's network name (hostname).
    """
    # Get the machine name using platform
    machine_name = platform.node()
    return machine_name

if __name__ == "__main__":
    """
    The main entry point of the script.
    
    This section:
    1. Calls the functions to get the machine's IP address and name.
    2. Prints the retrieved information.
    3. Prints a custom message.
    """
    # Get the machine's IP address
    ip = get_machine_ip()
    # Get the machine's name
    name = get_machine_name()
    # Print the machine's IP address and name
    print(f"Machine IP: {ip}")
    print(f"Machine Name: {name}")
    # Print a custom message
    print("my name is Helena")
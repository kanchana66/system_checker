import psutil

def get_system_info():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get RAM usage
    ram_info = psutil.virtual_memory()
    ram_usage = ram_info.percent

    # Get disk usage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent

    # Get network information
    network_info = psutil.net_io_counters()
    bytes_sent = network_info.bytes_sent
    bytes_received = network_info.bytes_recv

    # Construct a dictionary with the collected information
    system_info = {
        "CPU Usage (%)": cpu_usage,
        "RAM Usage (%)": ram_usage,
        "Disk Usage (%)": disk_usage,
        "Bytes Sent": bytes_sent,
        "Bytes Received": bytes_received
    }

    return system_info

# Example usage:
if __name__ == "__main__":
    system_info = get_system_info()

    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

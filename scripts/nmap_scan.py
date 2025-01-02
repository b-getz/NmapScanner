import nmap
import logging
from datetime import datetime
import matplotlib.pyplot as plt

# Configure logging
log_file = "nmap_scan_log.txt"
logging.basicConfig(
    filename="nmap_scan_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Initialize the Nmap scanner
scanner = nmap.PortScanner()

# Get user input for target and scan selection
target = input("Enter the target IP address of network range (e.g., 192.168.56.103 or 192.168.56.0/24): ")
print("Choose a scan: ")
print("1. Service Version Scan (-sV)")
print("2. Vulnerabilities Scan (--script vuln)")
scan_choice = input("Enter choice (1 or 2): ")

# Set Nmap arguments based on choice
if scan_choice == "1":
    arguments = "-sV"
elif scan_choice == "2":
    arguments = "--script vuln"
else:
    print("Invalid choice. Defaulting to Service Version Scan (-sV).")
    arguments = "-sV"

# Run the scan
print(f"Starting Nmap scan on {target} with arguments '{arguments}'...")
logging.info(f"Started scan on target {target} with arguments '{arguments}'")

try:
    scan_result = scanner.scan(hosts=target, arguments=arguments)

    # Parse the scan results
    ports = []
    services = []
    for port, details in scanner[target]['tcp'].items():
        ports.append(port)
        services.append(details['name'])
    
    # Generate a refined bar chart of open ports
    sorted_ports_services = sorted(zip(ports, services))
    ports, services = zip(*sorted_ports_services)

    # Generate a bar chart of open ports
    plt.figure(figsize=(12, 8))
    plt.bar(ports,[1] * len(ports), tick_label=services, width=0.5)
    plt.xlabel('Ports')
    plt.ylabel('Open Status')
    plt.title(f'Open ports and Services for {target}')
    plt.xticks(rotation=60)
    plt.tight_layout()

    # Save the chart
    chart_file = f"nmap_scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(chart_file)
    print(f"Chart saved as {chart_file}.")
    logging.info(f"Visualization saved as {chart_file}.")

    # Save the results
    output_file = f"nmap_scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, "w") as file:
        file.write(f"Scan results for {target}:\n")
        file.write(scanner.csv())

    print(f"Scan complete! Results saved to {output_file}.")
    logging.info(f"Scan complete. Results saved to {output_file}.")
except Exception as e:
    print(f"An error occured: {e}")
    logging.error(f"An error ocured during the scan: {e}")

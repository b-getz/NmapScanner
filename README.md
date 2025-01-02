# Nmap Scanner
This project is a Python-based tool for network scanning using Nmap. It is designed to perform detailed scans of networks, identify open ports and services, and generate outputs in multiple formats.

# Features
- **Interactive User Input**:
  - Enter specific target IP addresses or network ranges.
  - Choose between Service Detection ('-sV') and Scanning for Vulnerabilities ('--script vuln').
- **Scan Outputs**:
  - Saves results in a '.txt' file.
  - Logs all scan activities in a dedicated log file.
  - Optional visualization of open ports and services as bar charts(work in progress).

# Pre-requisites
- Python 3.x
- Nmap installed
- Requires Python libraries:
  - 'python-nmap'
  - 'matplotlib'

# Setup Instructions & Usage
1. Clone the repository:
   ```bash
   git clone https://github/b-getz/NmapScanner.git
2. Navigate to the project folder:
   ```bash
   cd NmapScanner
3. Install the required libraries
   ```bash
   pip install python-nmap matplotlib
4. Run the main scanner script:
   ```bash
   python3 scripts/nmap_scan.py
5. Enter the target IP address or network range (e.g., 192.168.56.103 or 192.168.56.0/24)
6. Choose a scan (-sV or --script vuln)
7. View the saved results (stored in results/, logs/, charts/)

# Testing Environment
This tool was test on the following environment:
- **Metasploitable**: A vulnerable virtual machine designed for educational and testing purposes.
- Hosted in a local VirtualBox setup isolated from external networks.

# Disclaimer
This tool is intended for **educational purposes** and should **ONLY** be used on owned networks. Unauthorized use of this tool on networks could result in the violation of local laws and regulations.

# Future Enhancements
1. Improved visualization in regards to charts
2. Additional user options

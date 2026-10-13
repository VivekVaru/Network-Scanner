# Network Scanner

A beginner-friendly TCP network scanner built with Python to explore network security fundamentals, TCP port scanning, service identification, and basic banner grabbing.

## Overview

Network Scanner is a command-line cybersecurity project designed for authorized systems and local lab environments. It scans a target IPv4 address for open TCP ports and displays useful information through a colorful terminal interface.

The project demonstrates Python programming, socket networking, multithreading, input validation, and basic scan reporting.

## Features

- **IP validation:** Validates the target IP address before scanning.
- **Multiple scan options:** Supports custom port ranges, common TCP ports, and all TCP ports from 1 to 65535.
- **Multithreading:** Uses `ThreadPoolExecutor` to scan ports concurrently.
- **Live progress:** Displays scan progress and discovered open ports.
- **Service identification:** Looks up service names using a local CSV database.
- **Banner grabbing:** Attempts to retrieve service banners from open ports.
- **Scan statistics:** Reports the number of ports scanned, open ports, elapsed time, and scan speed.
- **Text reports:** Saves scan results in the local `reports/` directory.
- **Colorful terminal UI:** Uses a separate Python module for terminal presentation.
- **Portable file paths:** Uses `pathlib` to locate project resources.

## Technologies Used

- Python 3
- Socket programming
- `ipaddress`
- `concurrent.futures`
- CSV file handling
- `pathlib`
- Git and GitHub

The scanner uses Python's standard library and does not require third-party Python packages.

## Project Structure

```text
Network-Scanner/
├── scanner1.py
├── UI.py
├── port_services.csv
├── requirements.txt
├── .gitignore
├── README.md
└── reports/             # Generated locally; excluded from Git
```

## Requirements

- Python 3
- Windows, Linux, or another compatible Python environment
- Git is optional if you only want to run the scanner

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/VivekVaru/Network-Scanner.git
cd Network-Scanner
```

### 2. Run the scanner

On Windows:

```powershell
python scanner1.py
```

On Linux:

```bash
python3 scanner1.py
```

No external dependencies need to be installed.

## Usage

Start the program and follow the interactive terminal prompts.

### Step 1: Enter a target IP address

For a local test, use:

```text
127.0.0.1
```

### Step 2: Select a scan option

The scanner provides three options:

| Option | Description |
|---|---|
| Custom port range | Scans a specified range, such as ports 1–1000 |
| All ports | Scans TCP ports 1–65535 |
| Common ports | Scans a predefined list of commonly used TCP ports |

### Step 3: Review the results

During the scan, the terminal displays progress and discovered open ports. At completion, it displays scan statistics and the path to the generated report.

## Example Output

The following is an illustrative example of the output format. Actual results depend on the target system.

```text
Enter target IP address: 127.0.0.1

PORT SCAN OPTIONS
[1] Custom port range
[2] All ports
[3] Common ports

Enter your choice: 3

SCAN PROGRESS
[========================] 100.0%

OPEN PORTS
[+] Port 8080 is OPEN | Service: Unknown

SCAN COMPLETE
Target              : 127.0.0.1
Total ports scanned : 15
Total open ports    : 1
Scan time           : 0.50 seconds
Scan speed           : 30.00 ports/second

[+] Report saved successfully:
reports/scan_report_<timestamp>.txt
```

The values and port shown above are examples, not guaranteed scan results. The terminal formatting may vary slightly.

## Report Generation

After a scan completes, the program generates a timestamped text report in the `reports/` directory.

Reports include:

- Target IP address
- Scan type and port range
- Total ports scanned
- Number of open ports
- Scan duration and speed
- Open-port details, service names, and available banners

Generated reports are kept locally and excluded from the public Git repository by `.gitignore`.

## Limitations

- Scans TCP ports only; UDP scanning is not implemented.
- Service identification uses a local CSV mapping and may not always reflect the actual service running on a port.
- Banner grabbing depends on whether the target service returns a readable banner.
- Firewalls, network conditions, connection timeouts, and thread scheduling can affect scan results and duration.
- The scanner is a learning project, not a replacement for a full-featured professional network assessment tool.

## Ethical Use

Use this tool only on localhost, systems you own, or systems for which you have explicit authorization to perform security testing.

Scanning systems without permission may violate laws, policies, or terms of service. You are responsible for ensuring that your use is authorized and lawful.

## Future Improvements

- Export reports in JSON or CSV format.
- Add configurable timeout and worker settings.
- Improve service fingerprinting.
- Add unit tests and automated testing.
- Improve report formatting and error handling.
- Add screenshots and usage demonstrations to the documentation.

## Author

**Vivek Varu**

GitHub: [@VivekVaru](https://github.com/VivekVaru)

---

This project was developed as a hands-on learning exercise in Python programming, TCP networking, and cybersecurity fundamentals.

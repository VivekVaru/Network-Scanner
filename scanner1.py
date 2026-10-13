import socket
import ipaddress
import time
import csv
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from UI import (
    show_banner,
    show_startup,
    green,
    yellow,
    red,
    cyan,
    white
)


# ==========================================
# Common TCP Ports
# ==========================================

COMMON_PORTS = [
    21,      # FTP
    22,      # SSH
    23,      # Telnet
    25,      # SMTP
    53,      # DNS
    80,      # HTTP
    110,     # POP3
    135,     # RPC
    139,     # NetBIOS
    143,     # IMAP
    443,     # HTTPS
    445,     # SMB
    3306,    # MySQL
    3389,    # RDP
    8080     # HTTP Alternative
]


# ==========================================
# Get Target IP Address
# ==========================================

def get_target():
    while True:
        target = input(
            cyan("Enter target IP address: ")
        ).strip()

        try:
            ipaddress.ip_address(target)
            return target
        except ValueError:
            print(red("Invalid IP address. Please try again."))


# ==========================================
# Choose Ports to Scan
# ==========================================

def choose_ports():
    print()
    print(cyan("=" * 40))
    print(yellow("             PORT SCAN OPTIONS"))
    print(cyan("=" * 40))
    print()

    print(green("[1] Custom port range"))
    print(green("[2] All ports"))
    print(green("[3] Common ports"))
    print()

    while True:
        choice = input(
            yellow("Enter your choice: ")
        ).strip()

        if choice == "1":
            while True:
                try:
                    start_port = int(
                        input(cyan("Enter starting port: "))
                    )
                    end_port = int(
                        input(cyan("Enter ending port: "))
                    )

                    if (
                        not 1 <= start_port <= 65535
                        or not 1 <= end_port <= 65535
                    ):
                        print(red("Ports must be between 1 and 65535."))
                        continue

                    if start_port > end_port:
                        print(
                            red(
                                "Starting port cannot be greater "
                                "than ending port."
                            )
                        )
                        continue

                    return (
                        list(range(start_port, end_port + 1)),
                        "Custom Range",
                        f"{start_port}-{end_port}"
                    )

                except ValueError:
                    print(red("Please enter valid port numbers."))

        elif choice == "2":
            return (
                list(range(1, 65536)),
                "All Ports",
                "1-65535"
            )

        elif choice == "3":
            return (
                COMMON_PORTS,
                "Common Ports",
                "Common Port List"
            )

        else:
            print(red("Invalid choice. Please enter 1, 2, or 3."))


# ==========================================
# Scan a Single TCP Port
# ==========================================

def scan_port(target, port, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        result = s.connect_ex((target, port))
        if result == 0:
            return port
        return None
    except OSError:
        return None
    finally:
        s.close()


# ==========================================
# Attempt to Grab a Service Banner
# ==========================================

def grab_banner(target, port, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        s.connect((target, port))
        banner = s.recv(1024)

        if banner:
            return banner.decode(
                "utf-8",
                errors="ignore"
            ).strip()

        return None

    except (socket.timeout, ConnectionError, OSError):
        return None
    finally:
        s.close()


# ==========================================
# Load Service Information from CSV
# ==========================================

def load_services():
    services = {}
    file_path = Path(__file__).resolve().parent / "port_services.csv"

    try:
        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    port = int(row["port"])
                    protocol = row["protocol"].strip().lower()
                    service = row["service"].strip()

                    if protocol == "tcp":
                        services[port] = service

                except (
                    ValueError,
                    KeyError,
                    AttributeError,
                    TypeError
                ):
                    continue

    except FileNotFoundError:
        print()
        print(yellow("Warning: port_services.csv was not found."))
        print(yellow("Service names will be shown as Unknown."))

    return services


# ==========================================
# Generate Scan Report
# ==========================================

def generate_report(
    target,
    scan_type,
    port_range,
    total_ports,
    scan_results,
    scan_time,
    scan_speed
):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    reports_dir = Path(__file__).resolve().parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_file = reports_dir / f"scan_report_{timestamp}.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("NETWORK SCANNER REPORT\n")
        file.write("======================\n\n")
        file.write(f"Target: {target}\n")
        file.write(f"Scan Type: {scan_type}\n")
        file.write(f"Port Range: {port_range}\n")
        file.write(f"Total Ports Scanned: {total_ports}\n")
        file.write(f"Total Open Ports: {len(scan_results)}\n")
        file.write(f"Scan Time: {scan_time:.2f} seconds\n")
        file.write(f"Scan Speed: {scan_speed:.2f} ports/second\n\n")
        file.write("OPEN PORTS\n")
        file.write("==========\n\n")

        if scan_results:
            for result in scan_results:
                file.write(f"Port: {result['port']}\n")
                file.write(f"State: {result['state']}\n")
                file.write(f"Service: {result['service']}\n")
                file.write(
                    f"Banner: {result['banner'] if result['banner'] else 'None'}\n"
                )
                file.write("\n")
        else:
            file.write("No open ports found.\n")

    print()
    print(green("[+] Report saved successfully:"))
    print(cyan(str(report_file)))


# ==========================================
# Display Scan Information
# ==========================================

def show_scan_information(
    target,
    scan_type,
    port_range,
    total_ports,
    max_workers,
    timeout
):
    print()
    print(cyan("=" * 50))
    print(yellow("                 SCAN CONFIGURATION"))
    print(cyan("=" * 50))
    print()

    print(white(f"Target        : {target}"))
    print(white(f"Scan Type     : {scan_type}"))
    print(white(f"Port Range    : {port_range}"))
    print(white(f"Ports to Scan : {total_ports}"))
    print(white(f"Workers       : {max_workers}"))
    print(white(f"Timeout       : {timeout} seconds"))
    print()


# ==========================================
# Build Progress Bar Text
# ==========================================

def build_progress_text(completed, total_ports, open_ports_count):
    percentage = (
        completed / total_ports * 100
        if total_ports else 100
    )

    bar_length = 24
    filled_length = int(bar_length * percentage / 100)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)

    return (
        f"{cyan('[*]')} "
        f"{green('[' + bar + ']')} "
        f"{yellow(f'{percentage:5.1f}%')} "
        f"| Completed: {completed}/{total_ports} "
        f"| Open: {open_ports_count}"
    )


# ==========================================
# Update Progress Line Without Repeating It
# ==========================================

def update_progress_line(completed, total_ports, open_ports_count):
    progress_text = build_progress_text(
        completed,
        total_ports,
        open_ports_count
    )

    # The progress line is followed by a blank line, three
    # section-heading lines, another blank line, and each
    # discovered port occupies exactly one line.
    rows_up = open_ports_count + 6

    # Move up to the progress line, replace it, and return
    # to the start of the output line below the port list.
    print(f"\033[{rows_up}A", end="")
    print("\r\033[2K" + progress_text, end="")
    print("\r", end="")
    print(f"\033[{rows_up}B", end="")
    print("\r", end="", flush=True)


# ==========================================
# Main Program
# ==========================================

def main():
    show_banner()
    show_startup()

    target = get_target()
    ports, scan_type, port_range = choose_ports()
    services = load_services()

    max_workers = 100
    timeout = 0.3
    total_ports = len(ports)

    show_scan_information(
        target,
        scan_type,
        port_range,
        total_ports,
        max_workers,
        timeout
    )

    print(yellow("[*] Starting TCP scan..."))
    print()

    scan_results = []
    completed = 0
    open_ports_count = 0

    print(cyan("[*] SCAN PROGRESS"))
    print(build_progress_text(0, total_ports, 0))
    print()
    print(cyan("=" * 50))
    print(yellow("                    OPEN PORTS"))
    print(cyan("=" * 50))
    print()

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(scan_port, target, port, timeout): port
            for port in ports
        }

        for future in as_completed(futures):
            open_port = future.result()
            completed += 1

            if open_port is not None:
                service = services.get(open_port, "Unknown")
                banner = grab_banner(target, open_port, timeout)

                result = {
                    "port": open_port,
                    "state": "OPEN",
                    "service": service,
                    "banner": banner
                }

                scan_results.append(result)
                open_ports_count += 1

                message = (
                    f"[+] Port {open_port} is OPEN "
                    f"| Service: {service}"
                )

                if service == "Unknown":
                    print(yellow(message))
                else:
                    print(green(message))

            if (
                completed % 100 == 0
                or open_port is not None
                or completed == total_ports
            ):
                update_progress_line(
                    completed,
                    total_ports,
                    open_ports_count
                )

    end_time = time.time()
    scan_time = end_time - start_time
    scan_speed = total_ports / scan_time if scan_time > 0 else 0

    scan_results.sort(key=lambda result: result["port"])

    print()
    print()
    print(cyan("=" * 40))
    print(yellow("               SCAN COMPLETE"))
    print(cyan("=" * 40))
    print()

    print(white(f"Target              : {target}"))
    print(white(f"Total ports scanned : {total_ports}"))
    print(white(f"Total open ports    : {len(scan_results)}"))
    print(white(f"Scan time           : {scan_time:.2f} seconds"))
    print(white(f"Scan speed          : {scan_speed:.2f} ports/second"))

    # The live OPEN PORTS section already displayed the results,
    # so don't print a second copy at the end.

    generate_report(
        target,
        scan_type,
        port_range,
        total_ports,
        scan_results,
        scan_time,
        scan_speed
    )


# ==========================================
# Program Entry Point
# ==========================================

if __name__ == "__main__":
    main()

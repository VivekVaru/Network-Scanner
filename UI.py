
# ==========================================
# Network Scanner - User Interface
# ==========================================

import time


# ==========================================
# Terminal Colors
# ==========================================

RESET = "\033[0m"

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BLUE = "\033[94m"
WHITE = "\033[97m"


# ==========================================
# UI Helper Functions
# ==========================================

def green(text):
    return f"{GREEN}{text}{RESET}"


def yellow(text):
    return f"{YELLOW}{text}{RESET}"


def red(text):
    return f"{RED}{text}{RESET}"


def cyan(text):
    return f"{CYAN}{text}{RESET}"


def blue(text):
    return f"{BLUE}{text}{RESET}"


def white(text):
    return f"{WHITE}{text}{RESET}"


# ==========================================
# Network Scanner Logo
# ==========================================

def show_banner():

    print()

    print(green(r"""
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""))

    print(yellow(
        "              PYTHON NETWORK SCANNER"
    ))

    print(cyan(
        "        Fast | Multithreaded | TCP Scanner"
    ))

    print()


# ==========================================
# Startup Sequence
# ==========================================

def show_startup():

    print(cyan("=" * 60))

    print(yellow("[*] Initializing scanner..."))
    time.sleep(0.4)

    print(yellow("[*] Loading service database..."))
    time.sleep(0.4)

    print(yellow("[*] Preparing scan engine..."))
    time.sleep(0.4)

    print()

    print(green("[+] Scanner ready!"))

    print(cyan("=" * 60))

    print()


# ==========================================
# Program Entry Point
# ==========================================

if __name__ == "__main__":

    show_banner()
    show_startup()

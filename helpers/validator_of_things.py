from colorama import Fore,Style
import re
from typing import Any

def validate_ipv4(ip:str) -> bool:
    regex_ipv4: Any = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
    validate_ip: Any = re.match(regex_ipv4,ip)
    
    if validate_ip is not None:
        return True
    else:
        print(f"Bad format ip {Fore.RED + ip}" + Style.RESET_ALL)
        return False

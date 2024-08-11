from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException
)
from typing import Dict,Tuple

def send_command_to_device(device:Dict,command:str) -> Dict:
    """ Execute a command """
    
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in command:
                output: str = ssh.send_command(command)
                result[command] = output
        return result
    
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        return 'Timeout Error / Authentication Error'
    

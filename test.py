import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

from pprint import pprint
from helpers import ConnectionSsh


device = {
    "device_type": "mikrotik_routeros",
    "host": "192.168.100.1",
    "username": "scripts",
    "password": "scripting"
}

command = 'interfaces print'

ConnectionSsh.send_command_to_device(device,command)
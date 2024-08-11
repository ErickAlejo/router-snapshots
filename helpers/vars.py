def conf_connection(host,username="something",password="something") -> dict:
    device = {
        "device _type": "mikrotik_routeros",
        "host": host,
        "username": username,
        "password": password
    }
    
    return device
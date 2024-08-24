import datetime

def conf_connection(host,username="something",password="something") -> dict:
    device = {
        "device _type": "mikrotik_routeros",
        "host": host,
        "username": username,
        "password": password
    }
    
    return device

date = datetime.datetime.now()
date_full = date.strftime("%B %d %Y %X")
path_database_prod = "databases/snapshots.db" 
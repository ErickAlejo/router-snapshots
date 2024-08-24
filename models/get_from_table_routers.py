# Models to use
from models.add_db_main_and_tables import Routers
from typing import Any, Iterable

# Helpers
from helpers.vars import conf_connection
from helpers.vars import path_database_prod
from helpers.ConnectionDb import init_connection_to_db
from helpers.ConnectionSsh import send_command_to_device

def get_all_ips_from_db() -> list:
    session = init_connection_to_db(path_database_prod)
    routers = session.query(Routers).all()
    
    ip = []
    for router in routers:
        ip.append(router.router_ip)

    return ip

def get_output_of_routers(ip) -> str:
    device = conf_connection(ip) 
    output = send_command_to_device(device,"/interface print detail without-paging")    

    return output        

def add_new_router(name,ip) -> None:
    try:
            
        session = init_connection_to_db(path_database_prod)
        router_01 = Routers(
            router_alias=name,
            router_ip=ip)
        
        session.add(router_01)
        session.commit()
        session.close()
        
        print(f"\n(DB) New router added - {ip}")

    except Exception as err:
        raise err
    
    finally:
        session.commit()
        session.close()
        
    
def get_id_of_router(ip) -> str | None:
    
    try:
        session: Any = init_connection_to_db(path_database_prod)
        id_router_object: Iterable = session.query(Routers.router_id).where(Routers.router_ip == ip)
        
        id_router_string: list = [id_str for id_str in id_router_object]
        
        if len(id_router_string) > 0:
            return id_router_string[0][0]
        else:
            return None
    
    except Exception as err:
        raise err
    
    finally:
        session.commit()
        session.close()
        
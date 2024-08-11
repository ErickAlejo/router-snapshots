# Helpers
from typing import Any
import argparse
from helpers.ConnectionSsh import send_command_to_device
from helpers.vars import conf_connection
from helpers.validator_of_things import validate_ipv4

# SQL and tables abstraction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.create_main_tables import Routers

# Lib native neccesary
from pprint import pprint
import re

 
def init_arguments() -> Any:
    parse = argparse.ArgumentParser(
        prog='MikroDeck',
        description='Save Snapshot of your routers',
        epilog='Made with Python3.10 <3\n'
    )
    parse.add_argument('--routers','-r',type=str,nargs="+",help="Max 5 ips, if you need add more ips, so use --from-file flag")
    parse.add_argument('--from-file','-ff',help="")
    parse.add_argument('--selectdb','-sdb',help="")  
    args = parse.parse_args()
    
    return args

def init_connection_to_db(path_db:str) -> Any:
    engine = create_engine(f"sqlite:///{path_db}", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    return session

def get_all_ips_from_db() -> list:
    session = init_connection_to_db("databases/snapshots.db")
    routers = session.query(Routers).all()
    
    ip = []
    for router in routers:
        ip.append(router.router_ip)

    return ip

def get_output_of_routers(ip) -> str:
    device = conf_connection(ip) 
    output = send_command_to_device(device,"/interface print detail without-paging")    

    return output        

def handle_every_argument_passed_to_main_script(args):

    if args.routers is not None:
        # Validate
        if len(args.routers) > 0 and len(args.routers) <= 10:
            for ip in args.routers:
                good_format = validate_ipv4(ip)     
                if good_format is True:
                    pass
                else:
                    break
                             
    elif args.from_file is not None:
        pass
    elif args.selectdb is not None:
        pass  

try:
    args = init_arguments()
    ips = get_all_ips_from_db()
    print('\n\n')
    handle_every_argument_passed_to_main_script(args)

except Exception as err:
    raise err

finally:
    print("\nEnd ...")
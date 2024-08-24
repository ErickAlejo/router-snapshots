# Native imports
from typing import Any
import argparse

# Helpers
from helpers.validator_of_things import validate_ipv4

# Base (Logics)
from router_argument import run_routers


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

def handle_every_argument_passed_to_main_script(args) -> None:

    if args.routers is not None:
        # Validate if exist argument routers
        
        if len(args.routers) > 0 and len(args.routers) <= 10:
            for ip in args.routers:
                good_format = validate_ipv4(ip)     
                if good_format is True:
                    run_routers(ip)
                else:
                    break
                             
    elif args.from_file is not None:
        pass
    elif args.selectdb is not None:
        pass  

try:
    args = init_arguments()
    print('\n\n')
    handle_every_argument_passed_to_main_script(args)

except Exception as err:
    raise err

finally:
    print("\nEnd ...")
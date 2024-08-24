import uuid
from typing import Any,Iterable
from helpers.vars import date_full

# Helpers
from helpers.ConnectionDb import init_connection_to_db
from helpers.ConnectionSsh import send_command_to_device

# Models
from models.get_from_table_routers import add_new_router
from models.get_from_table_routers import get_id_of_router

# Tables
from models.add_db_main_and_tables import Routers
from models.add_db_main_and_tables import Commands
from models.add_db_main_and_tables import Output


def run_routers(ip) -> None:
    try:
            
        session: Any = init_connection_to_db('databases/snapshots.db')
        list_commands: Iterable = session.query(Commands.command_name,Commands.command_id).all()
        
        router: Iterable = session.query(Routers.router_id).where(Routers.router_ip == ip)    
        device: list = [routers for routers in router]
        
        id_router = ''
        
        # If router not exist so added with generic name
        if len(device) == 0 : 
        
            while True:
                print(f"\n(DB) Not found your router - '{ip}'")
                answer = input("(DB) Do you want add it? (y/n) : ")   
                print("(Note) This devices will upload with name generic\n") 
                device = 'empty'
                
                if answer == 'y' or answer == 'Y':
                    # Generate UUID unique
                    unique_id = uuid.uuid4()

                    # Transform to string
                    unique_id_str = str(unique_id)
                    
                    # Add router in db
                    add_new_router(unique_id_str,ip)
                    
                    # Get his id
                    id_router = get_id_of_router(ip)
                    
                elif  answer == 'n' or answer == 'N':
                    break
        
        else:
            id_router = get_id_of_router(ip)
   
        save_output = ""
        for command in list_commands:
            print(command)
            
            output = send_command_to_device(ip,command[0])
            print(output)
            save_output = Output(output_command_name_fk = command[1], output_router_id_fk = id_router, output_text = output, output_time_log = date_full)
            
                
    except Exception as err:
        raise err

    finally:
        session.add(save_output)
        session.commit()
        session.close()
        
    
run_routers('Z.Z.Z.Y') 
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

# Tables
from models.create_main_tables import Routers
from models.create_main_tables import TypeCommands
from models.create_main_tables import Commands
from models.create_main_tables import Output

# Helpers
from helpers.FileHandle import open_file_txt
from colorama import Fore,Style


engine = create_engine("sqlite:///databases/testing.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def load_folder_data_testing(path:str) -> str:
    print('\n')
    interfaces_large_output: List[str] = open_file_txt(path) 
    
    if interfaces_large_output is not False:
        output_pretty: str = ""
        
        for out in range(len(interfaces_large_output)):
            output_pretty += interfaces_large_output[out]
        
        print(Fore.GREEN + f"Created pretty format to upload - {path}" + Style.RESET_ALL)
        return output_pretty

    else:
        print(Fore.RED + f"\nReturn 'empty' to - {path}" + Style.RESET_ALL)
        return 'emtpy'


# Add new entry in table Routers
router_01 = Routers(
            router_alias='ROUTER_TESTING',
            router_vendor='Mikrotik',
            router_model='RB4011',
            router_ip='192.168.1.10')

# Add new entry in table TypeCommands
type_command = TypeCommands(type_subscription='standar-prints')

# Add new entry in table Commands
command_01 = Commands(command_name='interface print brief without-paging', command_descriptions="Get all interfaces brief without paging")
command_02 = Commands(command_name='interface print detail without-paging', command_descriptions="Get all interfaces with more detail than 'brief'")
command_03 = Commands(command_name='ip neighbor print brief without-paging', command_descriptions='View neighbors of router')
command_04 = Commands(command_name='ip neighbor print detail without-paging', command_descriptions='View neighbor more detailed')

# Add new entry in table Commands
type_command.commands.append(command_01)
type_command.commands.append(command_02)
type_command.commands.append(command_03)
type_command.commands.append(command_04)



# Add new entry in table Output
interfaces_brief_output = load_folder_data_testing('data/testing_interfaces.txt')
interfaces_detail_output = load_folder_data_testing('data/testing_interfaces_detail.txt')

ip_neighbor_detail_output = load_folder_data_testing('data/testing_ip_neighbor_detail.txt')
ip_neighbor_brief_output = load_folder_data_testing('data/testing_ip_neighbor.txt')

output_01 = Output(
    output_command_name_fk = '2',
    output_router_id_fk = '1',
    output_text = f"{interfaces_detail_output}",
    output_time_log = 'Sun Jul 28 03:43:16'
)

output_02 = Output(
    output_command_name_fk = '1',
    output_router_id_fk = '1',
    output_text = f"{interfaces_brief_output}",
    output_time_log = "Thu Aug  1 10:38:15"
)

output_03 = Output(
    output_command_name_fk = '3',
    output_router_id_fk = '1',
    output_text = f"{ip_neighbor_brief_output}",
    output_time_log = "Sat Aug 10 11:04:05"
)


try:
    print('\n')
    session.add(router_01)
    session.add(type_command)
    session.add(command_01)
    session.add(command_02)
    session.add(command_03)
    session.add(command_04)
    session.add(output_01)
    session.add(output_02)
    session.add(output_03)
    session.commit()
    session.close()
    print('\n')
    print(Fore.YELLOW + f"All tables ready to use - testing.db\n" + Style.RESET_ALL)

except sqlalchemy.exc.IntegrityError:
    # For more information about exceptions core
    # https://docs.sqlalchemy.org/en/20/core/exceptions.html
    
    print(Fore.RED + "\nError adding duplicate entry\n" + Style.RESET_ALL)
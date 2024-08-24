from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Tables
from models.add_db_main_and_tables import Routers
from models.add_db_main_and_tables import TypeCommands
from models.add_db_main_and_tables import Commands
from models.add_db_main_and_tables import Output

engine = create_engine("sqlite:///databases/testing.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

router_01 = Routers(
            router_alias='RouterA',
            router_vendor='Mikrotik',
            router_model='CSS610',
            router_ip='192.168.2.0')

router_02 = Routers(
            router_alias='RouterB',
            router_vendor='Mikrotik',
            router_model='CSS610',
            router_ip='192.168.1.1')

# Add new entry in table TypeCommands
type_command = TypeCommands(type_subscription='standar-prints')

# Add new entry in table Commands
command_01 = Commands(command_name='interface print brief without-paging', command_descriptions="Get all interfaces brief without paging")
command_02 = Commands(command_name='interface print detail without-paging', command_descriptions="Get all interfaces with more detail than 'brief'")
command_03 = Commands(command_name='ip neighbor print brief without-paging', command_descriptions='View neighbors of router')
command_04 = Commands(command_name='ip neighbor print detail without-paging', command_descriptions='View neighbor more detailed')

type_command.commands.append(command_01)
type_command.commands.append(command_02)
type_command.commands.append(command_03)
type_command.commands.append(command_04)



output_01 = Output(
    output_command_name_fk = '1',
    output_router_id_fk = '1',
    output_text = """
    Columns: NAME, TYPE, ACTUAL-MTU, L2MTU, MAX-L2MTU, MAC-ADDRESS
    #   NAME                             TYPE      ACTUAL-MTU  L2MTU  MAX-L2MTU  MAC-ADDRESS      
    0 R ether1                           ether           1500   1600       9586  48:8B:7C:3A:XX:FF
    1   qsfp28-1-1                       ether           9570   9570       9570  48:8B:7C:3A:XX:FF
    2   qsfp28-1-2                       ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    3   qsfp28-1-3                       ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    4   qsfp28-1-4                       ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    5   qsfp28-2-1                       ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    6   qsfp28-2-2                       ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    7   qsfp28-2-3                       ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    8   qsfp28-2-4                       ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    10   sfp28-2                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    11   sfp28-3                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    12   sfp28-4                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    13   sfp28-5                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    14   sfp28-6                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    15   sfp28-7                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    16   sfp28-8                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    17   sfp28-9                          ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    18   sfp28-10                         ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    19   sfp28-11                         ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    20   sfp28-12                         ether           1500   1584       9570  48:8B:7C:3A:XX:FF
    30 R lo0                              bridge          1500  65535             16:5F:30:1B:84:D0
    31 R subring_01                       vlan            2000   9566             38:8B:7C:3A:XX:FF
    32 R vrf_poisoned                     vrf            65536                    2A:79:EF:CC:67:18

    """,
    output_time_log = 'Sun Jul 28 03:43:16'
)


output_02 = Output(
    output_command_name_fk = '1',
    output_router_id_fk = '1',
    output_text = """ 
    #     NAME                                TYPE       ACTUAL-MTU L2MTU  MAX-L2MTU MAC-ADDRESS      
    0     ether1                               ether            1550  1550      10222 DC:3C:5E:B7:C4:0A
    1  R  ether2                               ether            9216  9216      10222 DC:3C:5E:B7:C4:0B
          ether3                               ether            9216  9216      10222 DC:3C:5E:B7:C4:0C
    3  R  ether4                               ether            9216  9216      10222 DC:3C:5E:B7:C4:0D
    4  R  ;;; 305-SW
          ether5                               ether            1500  1580      10222 DC:3C:5E:B7:C4:0E
    5     ;;; dell
          ether6                               ether            1500  1580      10222 DC:3C:5E:B7:C4:0F
    6  R  ether7                               ether            1500  1580      10222 DC:3C:5E:B7:C4:00
    7     ether8                               ether            1500  1580      10222 DC:3C:5E:B7:C4:01
          sfp-sfpplus2                         ether            9216  9216      10222 DC:3C:5E:B7:C4:09
    15 R  loopback_prueba                     bridge           1500 65535            16:B7:67:48:58:01
    """,
    output_time_log = "Thu Aug  1 10:38:15"
)

session.add(type)
session.add(output_02)
session.commit()
session.close()

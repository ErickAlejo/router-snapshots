from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Tables
from create_main_tables import Routers
from create_main_tables import TypeCommands
from create_main_tables import Commands
from create_main_tables import Output

engine = create_engine("sqlite:///databases/snapshots.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

router_01 = Routers(
            router_alias='COL_MDE_ALGO_PTR_01_AGG01',
            router_vendor='Mikrotik',
            router_model='CSS610',
            router_ip='X.X.X.X')
router_02 = Routers(
            router_alias='COL_MDE_ALGO_PTR_01_AGG02',
            router_vendor='Mikrotik',
            router_model='CSS610',
            router_ip='Z.Z.Z.Z')
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
    0 R ether1                           ether           1500   1600       9586  48:A9:8A:CA:6F:D8
    1   qsfp28-1-1                       ether           9570   9570       9570  48:A9:8A:CA:6F:C4
    2   qsfp28-1-2                       ether           1500   1584       9570  48:A9:8A:CA:6F:C5
    3   qsfp28-1-3                       ether           1500   1584       9570  48:A9:8A:CA:6F:C6
    4   qsfp28-1-4                       ether           1500   1584       9570  48:A9:8A:CA:6F:C7
    5   qsfp28-2-1                       ether           1500   1584       9570  48:A9:8A:CA:6F:C8
    6   qsfp28-2-2                       ether           1500   1584       9570  48:A9:8A:CA:6F:C9
    7   qsfp28-2-3                       ether           1500   1584       9570  48:A9:8A:CA:6F:CA
    8   qsfp28-2-4                       ether           1500   1584       9570  48:A9:8A:CA:6F:CB
    ;;; AGF_02_OLAS_SFP+1
    9 R sfp28-1                          ether           9570   9570       9570  48:A9:8A:CA:6F:CC
    10   sfp28-2                          ether           1500   1584       9570  48:A9:8A:CA:6F:CD
    11   sfp28-3                          ether           1500   1584       9570  48:A9:8A:CA:6F:CE
    12   sfp28-4                          ether           1500   1584       9570  48:A9:8A:CA:6F:CF
    13   sfp28-5                          ether           1500   1584       9570  48:A9:8A:CA:6F:D0
    14   sfp28-6                          ether           1500   1584       9570  48:A9:8A:CA:6F:D1
    15   sfp28-7                          ether           1500   1584       9570  48:A9:8A:CA:6F:D2
    16   sfp28-8                          ether           1500   1584       9570  48:A9:8A:CA:6F:D3
    17   sfp28-9                          ether           1500   1584       9570  48:A9:8A:CA:6F:D4
    18   sfp28-10                         ether           1500   1584       9570  48:A9:8A:CA:6F:D5
    19   sfp28-11                         ether           1500   1584       9570  48:A9:8A:CA:6F:D6
    20   sfp28-12                         ether           1500   1584       9570  48:A9:8A:CA:6F:D7
    21 R VLAN10_SW_03_AGF02_OLAS          vlan            1500   9566             48:A9:8A:CA:6F:CC
    22 R VLAN60-to-COL_MDE_OMAN_PE_AGG02  vlan            2000   9566             48:A9:8A:CA:6F:CC
    ;;; COL_MDE_EDGE_CN_02
    23 R VLAN1100_101_EDGE_02             vlan            2000   9562             48:A9:8A:CA:6F:CC
    ;;; COL_MDE_EDGE_CN_03
    24 R VLAN1103_101_EDGE_03             vlan            2000   9562             48:A9:8A:CA:6F:CC
    ;;; COL_MDE_EDGE_CN_06
    25 R VLAN1106_101_EDGE_06             vlan            2000   9562             48:A9:8A:CA:6F:CC
    ;;; COL_MDE_EDGE_CN_02
    26   VRRP_EDGE_02_subring_01          vrrp            2000   9562             00:00:5E:00:01:02
    ;;; COL_MDE_EDGE_CN_03
    27   VRRP_EDGE_03_subring_01          vrrp            2000   9562             00:00:5E:00:01:03
    ;;; COL_MDE_EDGE_CN_06
    28   VRRP_EDGE_06_subring_01          vrrp            2000   9562             00:00:5E:00:01:01
    29 R lo                               loopback       65536                    00:00:00:00:00:00
    30 R lo0                              bridge          1500  65535             26:6F:50:3B:87:CD
    31 R subring_01                       vlan            2000   9566             48:A9:8A:CA:6F:CC
    32 R vrf_poisoned                     vrf            65536                    3A:79:EF:CC:67:18

    """,
    output_time_log = 'Sun Jul 28 03:43:16'
)


output_02 = Output(
    output_command_name_fk = '1',
    output_router_id_fk = '1',
    output_text = """ 
    #     NAME                                TYPE       ACTUAL-MTU L2MTU  MAX-L2MTU MAC-ADDRESS      
    0     ether1                              ether            1550  1550      10222 DC:2C:6E:C8:C4:1A
    1  R  ether2                              ether            9216  9216      10222 DC:2C:6E:C8:C4:1B
    2     ;;; TO_COL_MED_MP_02_LAB sfpplus1
        ether3                              ether            9216  9216      10222 DC:2C:6E:C8:C4:1C
    3  R  ether4                              ether            9216  9216      10222 DC:2C:6E:C8:C4:1D
    4  R  ;;; 305-SW
        ether5                              ether            1500  1580      10222 DC:2C:6E:C8:C4:1E
    5     ;;; dell
        ether6                              ether            1500  1580      10222 DC:2C:6E:C8:C4:1F
    6  R  ether7                              ether            1500  1580      10222 DC:2C:6E:C8:C4:20
    7     ether8                              ether            1500  1580      10222 DC:2C:6E:C8:C4:21
    8  R  ;;; OMAN_PTR_01_AGG01 Ten 1/1/1
        sfp-sfpplus1                        ether            9216  9216      10222 DC:2C:6E:C8:C4:18
    9  R  ;;; TO_COL_MED_MP_01_LAB sfpplus1
        sfp-sfpplus2                        ether            9216  9216      10222 DC:2C:6E:C8:C4:19
    10  X  VLAN20_TO_COL_MDE_MP_01_LAB         vlan                                   DC:2C:6E:C8:C4:19
    11  X  VLAN30_PRUEBA                       vlan                                   DC:2C:6E:C8:C4:19
    12  R  VLAN40_TO_COL_MDE_AGP01_OPTO        vlan             2000  9212            DC:2C:6E:C8:C4:19
    13  R  VLAN3503_TO_COL_MDE_OMAN_PTR_01_... vlan             2000  9212            DC:2C:6E:C8:C4:18
    14  R  ;;; MPLS loopback
        lo0                                 bridge           1500 65535            9A:E3:BC:95:2D:7D
    15  R  loopback_prueba                     bridge           1500 65535            16:B7:67:58:68:01
    """,
    output_time_log = "Thu Aug  1 10:38:15"
)

# session.add(router_02)
# session.add(output_02)
# session.commit()
# session.close()

ifaces_text = session.query(Output.output_text).all()
import textfsm
with open('templates/interfaces.template') as template:
    templating = textfsm.TextFSM(template)
    
result_output =  templating.ParseText(ifaces_text[0][0])

for row in result_output:
    print(dict(zip(templating.header,row)))
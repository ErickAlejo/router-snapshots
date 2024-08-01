from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, mapped_column, Mapped

Base = declarative_base()

class Routers(Base):
    __tablename__ = 'Routers'
    
    router_id: Mapped[int] = mapped_column(primary_key=True)
    router_alias: Mapped[str] = mapped_column(nullable=False)
    router_vendor: Mapped[str]
    router_model: Mapped[str]
    router_ip: Mapped[str] = mapped_column(nullable=False)
    # Definir la relación con Output y especificar back_populates y cascade
    outputs: Mapped[list["Output"]] = relationship('Output', back_populates='router', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"router_id: {self.router_id}, router_alias: {self.router_alias}, router_ip: {self.router_ip}"
    

class TypeCommands(Base):
    __tablename__ = 'TypeCommands'
    
    type_id: Mapped[int] = mapped_column(primary_key=True)
    type_subscription: Mapped[str]
    # Definir la relación con Commands y especificar back_populates y cascade
    commands: Mapped[list["Commands"]] = relationship('Commands', back_populates='type_command', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"type_subscription: {self.type_subscription}"
    
    
class Commands(Base):
    __tablename__ = 'Commands'
    
    command_id: Mapped[int] = mapped_column(primary_key=True)
    command_descriptions: Mapped[str]
    command_name: Mapped[str] = mapped_column(nullable=False)
    type_id_fk: Mapped[int] = mapped_column(ForeignKey("TypeCommands.type_id"))
    # Definir la relación con TypeCommands y especificar back_populates
    type_command: Mapped["TypeCommands"] = relationship('TypeCommands', back_populates='commands')
    # Definir la relación con Output y especificar back_populates y cascade
    outputs: Mapped[list["Output"]] = relationship('Output', back_populates='command', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"command_id: {self.command_id}, command_name: {self.command_name}"


class Output(Base):
    __tablename__ = 'Output'
    
    output_id: Mapped[int] = mapped_column(primary_key=True)
    output_command_name_fk: Mapped[int] = mapped_column(ForeignKey('Commands.command_id'))
    output_router_id_fk: Mapped[int] = mapped_column(ForeignKey('Routers.router_id'))
    output_text: Mapped[str]
    output_time_log: Mapped[str]
    # Definir la relación con Commands y especificar back_populates
    command: Mapped["Commands"] = relationship('Commands', back_populates='outputs')
    # Definir la relación con Routers y especificar back_populates
    router: Mapped["Routers"] = relationship('Routers', back_populates='outputs')
    
    def __repr__(self) -> str:
        return f"output_id: {self.output_id}, output_command_name_fk: {self.output_command_name_fk}, output_text: {self.output_text}, output_time_log: {self.output_time_log}"

# Configurar la base de datos
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear y agregar instancias
router = Routers(router_alias='Router1', router_vendor='Vendor1', router_model='Model1', router_ip='192.168.1.1')
type_command = TypeCommands(type_subscription='Subscription1')
command1 = Commands(command_name='Command1', command_descriptions='Description1', type_command=type_command)
command2 = Commands(command_name='Command2', command_descriptions='Description2', type_command=type_command)
type_command.commands.append(command1)
type_command.commands.append(command2)

output1 = Output(output_text='Output1', output_time_log='2024-07-27', command=command1, router=router)
output2 = Output(output_text='Output2', output_time_log='2024-07-28', command=command2, router=router)
command1.outputs.append(output1)
command2.outputs.append(output2)
router.outputs.append(output1)
router.outputs.append(output2)

session.add(router)
session.add(type_command)
session.commit()

# Comprobar los registros en la base de datos
for r in session.query(Routers).all():
    print(f"Router: {r.router_alias}, Outputs: {[o.output_text for o in r.outputs]}")

for tc in session.query(TypeCommands).all():
    print(f"TypeCommands: {tc.type_subscription}, Commands: {[c.command_name for c in tc.commands]}")

for c in session.query(Commands).all():
    print(f"Command: {c.command_name}, Outputs: {[o.output_text for o in c.outputs]}")

for o in session.query(Output).all():
    print(f"Output: {o.output_text}, Command: {o.command.command_name}, Router: {o.router.router_alias}")

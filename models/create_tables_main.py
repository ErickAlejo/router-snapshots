from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, mapped_column, Mapped

Base = declarative_base()

class Routers(Base):
    __tablename__ = 'Routers'
    
    router_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    router_alias: Mapped[str] = mapped_column(nullable=False,unique=True)
    router_vendor: Mapped[str]
    router_model: Mapped[str]
    router_ip: Mapped[str] = mapped_column(nullable=False,unique=True)
    
    def __repr__(self) -> str:
        return f"router_id : {self.router_id} router_alias{self.router_alias} router_ip {self.router_ip}"
    

class TypeCommands(Base):
    __tablename__ = 'TypeCommands'
    
    type_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    type_subscription: Mapped[str] = mapped_column(unique=True)
    # Definir la relación con Commands y especificar back_populates y cascade
    commands: Mapped[list["Commands"]] = relationship('Commands', back_populates='type_command', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"type_subscription {self.type_subscription}"
    
    
class Commands(Base):
    __tablename__ = 'Commands'
    
    command_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    command_descriptions: Mapped[str]
    command_name: Mapped[str] = mapped_column(nullable=False,unique=True)
    type_id_fk: Mapped[int] = mapped_column(ForeignKey("TypeCommands.type_id"))
    # Definir la relación con TypeCommands y especificar back_populates
    type_command: Mapped["TypeCommands"] = relationship('TypeCommands', back_populates='commands')
    # Definir la relación con Output y especificar back_populates y cascade
    outputs: Mapped[list["Output"]] = relationship('Output', back_populates='command', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"command_id {self.command_id} command_name {self.command_name}"


class Output(Base):
    __tablename__ = 'Output'
    
    output_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    output_command_name_fk: Mapped[int] = mapped_column(ForeignKey('Commands.command_id'))
    output_router_id_fk: Mapped[int] = mapped_column(ForeignKey('Routers.router_id'))
    output_text: Mapped[str]
    output_time_log: Mapped[str]
    # Definir la relación con Commands y especificar back_populates
    command: Mapped["Commands"] = relationship('Commands', back_populates='outputs')
    
    def __repr__(self) -> str:
        return f"\
            id: {self.output_id},\
            command_name: {self.output_command_name_fk},\
            text: {self.output_text},\
            time: {self.output_time_log}\
        "

# Configurar la base de datos
engine = create_engine('sqlite:///databases/snapshots.db', echo=True)
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()
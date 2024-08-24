from sqlalchemy import create_engine, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, mapped_column, Mapped
from datetime import datetime

Base = declarative_base()

class Routers(Base):
    __tablename__ = 'Routers'
    
    router_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    router_alias: Mapped[str] = mapped_column(nullable=False, unique=True)
    router_ip: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    # Definir la relación con Output
    outputs: Mapped[list["Output"]] = relationship('Output', back_populates='router', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"'id': {self.router_id} alias: {self.router_alias} ip: {self.router_ip}"

class TypeCommands(Base):
    __tablename__ = 'TypeCommands'
    
    type_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type_description: Mapped[str] = mapped_column(unique=True, nullable=False)
    
    # Definir la relación con Commands
    commands: Mapped[list["Commands"]] = relationship('Commands', back_populates='type_command', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"type_description: {self.type_description}"
    
class Commands(Base):
    __tablename__ = 'Commands'
    
    command_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    command_description: Mapped[str]
    command_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    type_id_fk: Mapped[int] = mapped_column(ForeignKey("TypeCommands.type_id"), nullable=False)
    
    # Definir la relación con TypeCommands
    type_command: Mapped["TypeCommands"] = relationship('TypeCommands', back_populates='commands')
    
    # Definir la relación con Output
    outputs: Mapped[list["Output"]] = relationship('Output', back_populates='command', cascade='all, delete, delete-orphan')
    
    def __repr__(self) -> str:
        return f"command_id: {self.command_id} command_name: {self.command_name}"

class Output(Base):
    __tablename__ = 'Output'
    
    output_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    output_command_id_fk: Mapped[int] = mapped_column(ForeignKey('Commands.command_id'), nullable=False)
    output_router_id_fk: Mapped[int] = mapped_column(ForeignKey('Routers.router_id'), nullable=False)
    output_text: Mapped[str] = mapped_column(nullable=False)
    output_time_log: Mapped[str] = mapped_column(nullable=False, default=datetime.utcnow)
    
    # Definir la relación con Commands
    command: Mapped["Commands"] = relationship('Commands', back_populates='outputs')
    
    # Definir la relación con Routers
    router: Mapped["Routers"] = relationship('Routers', back_populates='outputs')
    
    # Añadir una restricción única en la combinación de output_router_id_fk, output_command_id_fk y output_time_log
    __table_args__ = (
        UniqueConstraint('output_router_id_fk', 'output_command_id_fk', 'output_time_log', name='_router_command_time_uc'),
        Index('idx_output_command_id_fk', 'output_command_id_fk'),
        Index('idx_output_router_id_fk', 'output_router_id_fk'),
    )
    
    def __repr__(self) -> str:
        return f"id: {self.output_id}, command_id: {self.output_command_id_fk}, router_id: {self.output_router_id_fk}, time: {self.output_time_log}"

# Configurar la base de datos
engine = create_engine('sqlite:///databases/snapshots.db', echo=True)
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

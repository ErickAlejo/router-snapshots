CREATE TABLE Routers (
    router_id INTEGER PRIMARY KEY AUTOINCREMENT,
    router_subscription_fk INTEGER NOT NULL,
    router_alias VARCHAR(100) NOT NULL UNIQUE,
    router_vendor VARCHAR(100),
    router_ip VARCHAR(15) NOT NULL UNIQUE,
    FOREIGN KEY (router_subscription_fk) REFERENCES TypeCommands(type_id)
);

CREATE TABLE TypeCommands (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_subscription VARCHAR(50) NOT NULL UNIQUE   

);

CREATE TABLE Commands (
    command_id INTEGER PRIMARY KEY,
    command_descriptions TEXT,
    command_name TEXT NOT NULL,
    type_id_fk INT NOT NULL,
    FOREIGN KEY (type_id_fk) REFERENCES TypeCommands(type_id)
);

CREATE TABLE RouterCommands (
    router_id INT,
    command_id INT,
    execute_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    output TEXT,
    PRIMARY KEY (router_id, command_id),
    FOREIGN KEY (router_id) REFERENCES Routers(router_id),
    FOREIGN KEY (command_id) REFERENCES Comandos(command_id)
);

 
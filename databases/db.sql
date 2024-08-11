CREATE TABLE IF NOT EXISTS "Routers" (
        router_id INTEGER NOT NULL, 
        router_alias VARCHAR NOT NULL, 
        router_vendor VARCHAR NOT NULL, 
        router_model VARCHAR NOT NULL, 
        router_ip VARCHAR NOT NULL, 
        PRIMARY KEY (router_id), 
        UNIQUE (router_alias), 
        UNIQUE (router_ip)
);
CREATE TABLE IF NOT EXISTS "TypeCommands" (
        type_id INTEGER NOT NULL, 
        type_subscription VARCHAR NOT NULL, 
        PRIMARY KEY (type_id), 
        UNIQUE (type_subscription)
);
CREATE TABLE IF NOT EXISTS "Commands" (
        command_id INTEGER NOT NULL, 
        command_descriptions VARCHAR NOT NULL, 
        command_name VARCHAR NOT NULL, 
        type_id_fk INTEGER NOT NULL, 
        PRIMARY KEY (command_id), 
        UNIQUE (command_name), 
        FOREIGN KEY(type_id_fk) REFERENCES "TypeCommands" (type_id)
);
CREATE TABLE IF NOT EXISTS "Output" (
        output_id INTEGER NOT NULL, 
        output_command_name_fk INTEGER NOT NULL, 
        output_router_id_fk INTEGER NOT NULL, 
        output_text VARCHAR NOT NULL, 
        output_time_log VARCHAR NOT NULL, 
        PRIMARY KEY (output_id), 
        FOREIGN KEY(output_command_name_fk) REFERENCES "Commands" (command_id), 
        FOREIGN KEY(output_router_id_fk) REFERENCES "Routers" (router_id), 
        UNIQUE (output_text)
);


--- Tricks

SELECT 
    o.output_time_log,
    r.router_alias,
    c.command_name

FROM
    Output o

INNER JOIN 
    routers as r ON o.output_router_id_fk = r.router_id

INNER JOIN 
    commands as c ON o.output_command_name_fk = c.command_id

WHERE r.router_alias = 'ROUTER_TESTING' AND output_time_log LIKE '%Sun Jul 28%';
-- create a table
CREATE TABLE IF NOT EXISTS unique_id (
    if INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256),
)
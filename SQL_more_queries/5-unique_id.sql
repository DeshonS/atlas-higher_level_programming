-- create a table
CREATE TABLE IF NOT EXISTS unique_id (
    if INT NOT NULL DEFAULT 1 DISTINCT,
    name VARCHAR(256),
)
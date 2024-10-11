-- creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
)
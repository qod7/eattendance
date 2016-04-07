CREATE DATABASE passion;
CREATE USER passion WITH PASSWORD 'attendance@passion';
ALTER ROLE passion SET client_encoding TO 'utf8';
ALTER ROLE passion SET default_transaction_isolation TO 'read committed';
ALTER ROLE passion SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE passion TO passion;

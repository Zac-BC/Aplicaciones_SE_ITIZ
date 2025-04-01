    -- CREAR USUARIO --
CREATE USER ardilluda_admin with password 'contrase;a';
ALTER USER ardilluda_admin with SUPERUSER;

    -- CREAR BASE DE DATOS --
DROP DATABASE IF EXISTS ardilludadb;
CREATE DATABASE ardilludadb;
GRANT ALL PRIVILEGES ON DATABASE ardilludadb TO ardilluda_admin;
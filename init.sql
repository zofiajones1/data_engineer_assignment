CREATE DATABASE application;
CREATE USER application WITH PASSWORD 'secretpassword';
grant all privileges on database application to application;
grant all privileges on database application to postgres;

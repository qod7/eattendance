# README #

Passion E-Attendance serverside code.

### What is this repository for? ###

* Django coders
* Version: 1.0

### How do I get set up? ###

* clone repo
* pip install -r requirements.txt
* migrate

### Contribution guidelines ###

* Write tests
* Pep8 formatting

### Who do I talk to? ###

* Ashish/Bidhan

### Database Setup ###

* CREATE DATABASE passion;
* CREATE USER passion WITH PASSWORD 'attendance@passion';
* ALTER ROLE passion SET client_encoding TO 'utf8';
* ALTER ROLE passion SET default_transaction_isolation TO 'read committed';
* ALTER ROLE passion SET timezone TO 'UTC';
* GRANT ALL PRIVILEGES ON DATABASE passion TO passion;
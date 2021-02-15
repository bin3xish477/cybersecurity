CREATE DATABASE app;

USE app;

CREATE TABLE Users (
	username VARCHAR(35),
	email VARCHAR(35),
	password VARCHAR(50)
);

INSERT INTO Users 
VALUES
	("james", "james@gmail.com", "password"),
	("mike", "mike@proton.com", "mikeisawesome"),
	("joker", "joker@batman.com", "jokerjoker123"),
	("ashley", "ashley@yahoo.com", "1234567abc"),
	("Daphne", "daph@gmail.com", "d@phne123abc");

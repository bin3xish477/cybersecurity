CREATE DATABASE marvel;

USE marvel;

CREATE TABLE characters (
	Name VARCHAR(35),
	SuperPower VARCHAR(150),
	gender BIT(1)	
);

INSERT INTO characters 
VALUES
	("Hulk", "Super Strength, Indestructable", 0),
	("Spiderman", "Siper senses and strength", 0),
	("Iron Man", "Intelligence, Advanced Armored Suit, Flight", 0),
	("Captain Marvel", "Super Strength, Flight", 1),
	("Black Widow", "Skilled Assassin", 1),
	("Scarlet Witch", "Magic wielder", 1);

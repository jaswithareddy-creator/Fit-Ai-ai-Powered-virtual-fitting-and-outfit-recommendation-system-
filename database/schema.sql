CREATE DATABASE FitAI;

USE FitAI;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE measurements (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    height DECIMAL(5,2),
    shoulder DECIMAL(5,2),
    chest DECIMAL(5,2),
    waist DECIMAL(5,2),
    hip DECIMAL(5,2),

    FOREIGN KEY (user_id)
    REFERENCES users(id)
);

CREATE TABLE outfits (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150),
    category VARCHAR(100),
    color VARCHAR(50),
    size VARCHAR(10),
    price DECIMAL(10,2)
);

CREATE TABLE recommendations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    outfit_id INT,
    recommended_size VARCHAR(10),
    score DECIMAL(5,2),

    FOREIGN KEY (user_id)
    REFERENCES users(id),

    FOREIGN KEY (outfit_id)
    REFERENCES outfits(id)
);

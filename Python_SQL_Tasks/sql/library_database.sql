CREATE DATABASE library_db;

USE library_db;

CREATE TABLE Books (
    Book_ID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(100) NOT NULL,
    Author VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Price DECIMAL(10,2) NOT NULL,
    Available BOOLEAN DEFAULT TRUE
);

CREATE TABLE Members (
    Member_ID INT PRIMARY KEY AUTO_INCREMENT,
    Member_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Phone VARCHAR(15) UNIQUE,
    Join_Date DATE NOT NULL
);

CREATE TABLE Borrow_Records (
    Borrow_ID INT PRIMARY KEY AUTO_INCREMENT,
    Book_ID INT NOT NULL,
    Member_ID INT NOT NULL,
    Borrow_Date DATE NOT NULL,
    Return_Date DATE,

    FOREIGN KEY (Book_ID)
        REFERENCES Books(Book_ID),

    FOREIGN KEY (Member_ID)
        REFERENCES Members(Member_ID),

    CONSTRAINT chk_return_date
        CHECK (Return_Date IS NULL OR Return_Date >= Borrow_Date)
);
USE library_db;

INSERT INTO Books
    (Title, Author, Category, Price, Available)
VALUES
    ('Python Programming', 'Mark Lutz', 'Programming', 850.00, TRUE),
    ('Clean Code', 'Robert C. Martin', 'Programming', 950.00, TRUE),
    ('Database System Concepts', 'Abraham Silberschatz', 'Database', 1100.00, TRUE),
    ('The Alchemist', 'Paulo Coelho', 'Fiction', 450.00, TRUE),
    ('Data Science Handbook', 'Jake VanderPlas', 'Data Science', 900.00, TRUE);


-- SAMPLE MEMBERS RECORDS
INSERT INTO Members
    (Member_Name, Email, Phone, Join_Date)
VALUES
    ('Srinivas', 'srinivas@gmail.com', '9876543210', '2026-01-10'),
    ('Krishna', 'krishna@gmail.com', '9876543211', '2026-02-15'),
    ('Vishnu', 'vishnu@gmail.com', '9876543212', '2026-03-20');


-- SAMPLE BORROW RECORDS
INSERT INTO Borrow_Records
    (Book_ID, Member_ID, Borrow_Date, Return_Date)
VALUES
    (1, 1, '2026-09-01', '2026-09-10'),
    (2, 2, '2026-09-05', '2026-09-15'),
    (3, 1, '2026-09-10', NULL),
    (4, 3, '2026-09-12', NULL);

-- READ 
SELECT Book_ID, Title, Author, Category, Price, Available FROM Books;

-- Update record
UPDATE Books SET Price = 1000.00 WHERE Book_ID = 1;

-- DELETE 
DELETE FROM Books WHERE Book_ID = 5;

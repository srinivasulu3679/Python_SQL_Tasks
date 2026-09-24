USE library_db;

-- CREATE VIEW Borrowed Book Report

CREATE VIEW borrowed_book_report AS
SELECT br.Borrow_ID, b.Book_ID, b.Title, b.Author, m.Member_ID, m.Member_Name, m.Email, br.Borrow_Date, br.Return_Date
FROM Borrow_Records br

INNER JOIN Books b
    ON br.Book_ID = b.Book_ID

INNER JOIN Members m
    ON br.Member_ID = m.Member_ID;


-- VIEW REPORT

SELECT *
FROM borrowed_book_report;

-- CHECK CREATED VIEWS

SHOW FULL TABLES
WHERE TABLE_TYPE = 'VIEW';

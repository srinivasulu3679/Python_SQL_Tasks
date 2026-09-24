USE library_db;

---- JOIN
SELECT br.Borrow_ID, b.Title, b.Author, m.Member_Name, m.Email, br.Borrow_Date, br.Return_Date
FROM Borrow_Records br
INNER JOIN Books b
    ON br.Book_ID = b.Book_ID
INNER JOIN Members m
    ON br.Member_ID = m.Member_ID;


--- GROUP BY
SELECT m.Member_ID, m.Member_Name,
COUNT(br.Borrow_ID) AS Total_Borrowed
FROM Members m
LEFT JOIN Borrow_Records br
    ON m.Member_ID = br.Member_ID
GROUP BY
    m.Member_ID,
    m.Member_Name;

--- ORDER BY
SELECT Book_ID, Title, Author, Category, Price FROM Books ORDER BY Price DESC;


-- 4. AGGREGATE FUNCTIONS
-- Total number of books
SELECT COUNT(*) AS Total_Books FROM Books;

-- Average book price
SELECT AVG(Price) AS Average_Price FROM Books;

-- Highest book price
SELECT MAX(Price) AS Highest_Price FROM Books;

-- Lowest book price
SELECT MIN(Price) AS Lowest_Price FROM Books;

-- Total value of all books
SELECT SUM(Price) AS Total_Book_Value FROM Books;




# Write your MySQL query statement below
WITH Cte AS (
    SELECT Customer_number, COUNT(Order_number) AS NumOrd
    FROM Orders
    GROUP BY Customer_number
)
SELECT Customer_number
FROM Cte
WHERE NumOrd = (SELECT MAX(NumOrd) FROM Cte);

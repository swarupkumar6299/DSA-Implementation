# Write your MySQL query statement below
SELECT d.name AS Department,
       e1.name AS Employee,
       e1.Salary AS Salary
FROM Employee e1
INNER JOIN Department d
ON e1.departmentID = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.Salary > e1.Salary
      AND e2.departmentID = e1.departmentID
);

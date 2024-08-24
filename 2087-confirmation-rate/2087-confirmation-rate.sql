# Write your MySQL query statement below
SELECT s.user_id,
       IFNULL(ROUND(c.confirmed_count / c.total_count, 2), 0.00) AS confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT user_id,
           COUNT(*) AS total_count,
           SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_count
    FROM Confirmations
    GROUP BY user_id
) c ON s.user_id = c.user_id;

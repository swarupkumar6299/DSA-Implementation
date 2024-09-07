# Write your MySQL query statement below
WITH cte AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
cte2 AS (
    SELECT player_id, DATE_ADD(first_login, INTERVAL 1 DAY) AS next_date
    FROM cte
)
SELECT 
    ROUND(
        (SELECT COUNT(DISTINCT a.player_id)
         FROM Activity a
         JOIN cte2 ON a.player_id = cte2.player_id AND a.event_date = cte2.next_date
        ) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 
        2
    ) AS fraction;

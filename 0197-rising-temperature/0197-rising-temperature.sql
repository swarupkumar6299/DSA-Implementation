# Write your MySQL query statement below
WITH ctc AS (
    SELECT *,
           DATE_ADD(recorddate, INTERVAL -1 DAY) AS yesterday_date,
           LAG(recorddate) OVER (ORDER BY recorddate) AS prev_recorddate,
           LAG(temperature) OVER (ORDER BY recorddate) AS prev_temp
    FROM weather
)
SELECT id
FROM ctc
WHERE yesterday_date = prev_recorddate
  AND temperature > prev_temp;

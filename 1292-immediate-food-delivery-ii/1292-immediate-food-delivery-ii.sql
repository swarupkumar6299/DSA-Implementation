# Write your MySQL query statement below
SELECT ROUND (AVG (IF(orderDate = deliveryDate, 1, 0)), 4) * 100
AS immediate_percentage
FROM 
(
    SELECT MIN(order_date) AS orderDate,
    MIN(customer_pref_delivery_date) AS deliveryDate
    FROM Delivery 
    WHERE order_date <= customer_pref_delivery_date
    GROUP BY customer_id
) AS newTable
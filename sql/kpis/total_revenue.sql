-- Total revenue generated in October 2019
SELECT SUM(price)::numeric(12, 2) AS total_revenue
FROM user_behavior_oct
WHERE event_type = 'purchase';
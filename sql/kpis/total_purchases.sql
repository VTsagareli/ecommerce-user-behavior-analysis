-- Total number of purchases in October 2019
SELECT COUNT(*) AS total_purchases
FROM user_behavior_oct
WHERE event_type = 'purchase';
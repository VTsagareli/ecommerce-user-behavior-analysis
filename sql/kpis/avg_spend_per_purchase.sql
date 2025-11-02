-- Average spend per purchase
SELECT AVG(price)::numeric(10, 2) AS avg_spend_per_purchase
FROM user_behavior_oct
WHERE event_type = 'purchase';
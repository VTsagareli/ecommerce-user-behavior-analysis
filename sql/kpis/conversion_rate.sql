-- Conversion rate = purchases / views
SELECT 
  (COUNT(CASE WHEN event_type = 'purchase' THEN 1 END)::numeric
   / COUNT(CASE WHEN event_type = 'view' THEN 1 END)) 
  AS conversion_rate
FROM user_behavior_oct;
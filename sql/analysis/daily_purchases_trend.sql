SELECT 
  event_date,
  COUNT(*) AS purchase_count
FROM user_behavior_oct
WHERE event_type = 'purchase'
GROUP BY event_date
ORDER BY event_date;
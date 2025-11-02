SELECT 
  event_hour,
  event_type,
  COUNT(*) AS event_count
FROM user_behavior_oct
WHERE event_type IN ('view', 'cart', 'purchase')
GROUP BY event_hour, event_type
ORDER BY event_hour, event_type;
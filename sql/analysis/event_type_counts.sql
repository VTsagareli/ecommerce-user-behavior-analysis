SELECT 
  event_type,
  COUNT(*) AS total_events
FROM user_behavior_oct
GROUP BY event_type
ORDER BY total_events DESC;
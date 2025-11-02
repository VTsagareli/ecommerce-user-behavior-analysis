-- Hour with the highest number of all events
SELECT 
  LPAD(event_hour::text, 2, '0') || ':00' AS peak_hour
FROM (
  SELECT event_hour, COUNT(*) AS event_count
  FROM user_behavior_oct
  GROUP BY event_hour
  ORDER BY event_count DESC
  LIMIT 1
) AS sub;
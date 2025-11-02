SELECT 
  main_category,
  ROUND(AVG(price)::NUMERIC, 2) AS avg_price,
  COUNT(*) AS num_purchases
FROM user_behavior_oct
WHERE event_type = 'purchase'
GROUP BY main_category
ORDER BY avg_price DESC;
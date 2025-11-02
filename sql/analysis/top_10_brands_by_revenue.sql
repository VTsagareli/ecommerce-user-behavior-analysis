SELECT 
  brand,
  ROUND(SUM(price)::NUMERIC, 2) AS total_revenue,
  COUNT(*) AS purchase_count
FROM user_behavior_oct
WHERE event_type = 'purchase'
  AND brand IS NOT NULL
GROUP BY brand
ORDER BY total_revenue DESC
LIMIT 10;
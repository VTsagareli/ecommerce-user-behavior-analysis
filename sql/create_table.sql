CREATE TABLE public.user_behavior_oct (
  event_time TIMESTAMP WITHOUT TIME ZONE,
  event_type TEXT,
  product_id BIGINT,
  category_id BIGINT,
  category_code TEXT,
  brand TEXT,
  price DOUBLE PRECISION,
  user_id BIGINT,
  user_session TEXT,
  main_category TEXT,
  event_date DATE,
  event_hour INTEGER,
  day_of_week TEXT,
  event_dayofweek INTEGER,
  event_month INTEGER,
  event_day INTEGER
);
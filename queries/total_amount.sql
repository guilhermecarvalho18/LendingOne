SELECT customer_name, SUM(amount) as total_spent
FROM LENDING_DB.LENDING_SCHEMA."MERGED_TABLE"
GROUP BY customer_name
ORDER BY total_spent DESC;
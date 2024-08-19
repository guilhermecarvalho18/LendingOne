SELECT TO_CHAR(transaction_date, 'YYYY-MM') as month, COUNT(*) as total_transactions
FROM LENDING_DB.LENDING_SCHEMA."MERGED_TABLE"
GROUP BY TO_CHAR(transaction_date, 'YYYY-MM')
ORDER BY month;

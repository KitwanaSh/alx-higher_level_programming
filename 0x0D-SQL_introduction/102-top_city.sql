-- This script gets the top 3 cities in August and jully
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY 1
ORDER BY 2 DESC LIMIT 3;

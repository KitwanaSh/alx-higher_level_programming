-- this script output the number of value in each score
SELECT score, COUNT(*) AS 'number'
FROM second_table GROUP BY score ORDER BY score DESC;

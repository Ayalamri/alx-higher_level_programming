-- Selecting the score and name from the second_table
-- Filtering records where the score is greater than or equal to 10
-- Ordering the results by score in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

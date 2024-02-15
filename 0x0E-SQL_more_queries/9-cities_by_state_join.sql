-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- Query to list all cities with their corresponding state names without using JOIN
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

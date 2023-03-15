-- ists all the cities of California that can be found in the database

SELECT cities.name
FROM cities, states
WHERE cities.id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;

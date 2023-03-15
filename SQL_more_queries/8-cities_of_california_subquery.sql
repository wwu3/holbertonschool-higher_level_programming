-- ists all the cities of California that can be found in the database

SELECT name
FROM cities
WHERE states.id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;

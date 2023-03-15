-- ists all the cities of California that can be found in the database

SELECT states.name, states.id
FROM cities
WHERE states.id = (
    SELECT states.id
    FROM cities
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;

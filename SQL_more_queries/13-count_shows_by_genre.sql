-- lists all genres and displays the number of shows linked to each.

SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC

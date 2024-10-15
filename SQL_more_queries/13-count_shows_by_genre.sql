-- lists all genres from database and displays the number of shows linked to each
SELECT tv_genres.name AS genres, COUNT(tv_show_genres.id) AS number_of_shows
ORDER BY number_of_shows DESC, genres ASC;
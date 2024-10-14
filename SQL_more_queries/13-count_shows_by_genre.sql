-- lists all genres from database and displays the number of shows linked to each
SELECT tv_genres.name AS genres, COUNT(tv_show_genres.show_id) AS number_of_shows
JOIN genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY number_of_shows DESC, tv_genres.name ASC;
-- lists all genres from database and displays the number of shows linked to each
SELECT tv_genres.name FROM tv_genres AS genres, COUNT(tv_show_genres.show_id) FROM tv_show_genres AS number_of_shows
JOIN genres ON tv_show_genres.id = genres_id
ORDER BY number_of_shows DESC, genres ASC;
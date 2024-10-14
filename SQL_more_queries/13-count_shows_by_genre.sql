-- lists all genres from database and displays the number of shows linked to each
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS genres, number_of_shows
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY number_of_shows DESC, tv_genres.name ASC;
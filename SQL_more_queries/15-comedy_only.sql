-- lists all comedy shows in database
SELECT tv_shows.title AS title FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
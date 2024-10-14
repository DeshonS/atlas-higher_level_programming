-- lists all shows in hbtn_0d_tvshows that have a genre linked
SELECT DISTINCT tv_shows.title, tv_genres.name FROM tv_shows
JOIN tv_genres ON tv_shows.id = tv_genres.id
ORDER BY tv_shows.title AND tv_show_genres.genre_id;
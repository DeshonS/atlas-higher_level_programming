-- lists all shows in hbtn_0d_tvshows that have a genre linked
SELECT DISTINCT shows.title, genres.name FROM shows
JOIN genres ON shows.genre_id = genres.id
ORDER BY shows.title;
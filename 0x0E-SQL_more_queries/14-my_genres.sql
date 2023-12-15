-- Uses the hbtn_0d_tvshows database to list all genres of the show Dexter
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	the genre name
-- Each record should display: tv_genres.name
-- Database name is passed as an argument of the mysql command
SELECT name
FROM tv_genres
JOIN tv_show_genres
ON  tv_genres.id = genre_id
JOIN tv_shows
ON tv_shows.id = show_id
WHERE title = 'Dexter'
ORDER BY name ASC;

-- Uses the hbtn_0d_tvshows database to list all Comedy shows in the database 
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	tv_shows.title
-- Each record should display: tv_shows.title
-- Database name is passed as an argument of the mysql command
SELECT title
FROM tv_shows
JOIN tv_show_genres
ON  tv_shows.id = show_id
JOIN tv_genres
ON genre_id = tv_genres.id
WHERE name = 'Comedy'
ORDER BY title ASC;
-- this uses MULTIPLE JOINS joining the first appearing table with the second and the second with the third...

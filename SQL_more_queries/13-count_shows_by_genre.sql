-- man life is so sad bro
SELECT TV_SHOW_GENRES.genre AS genre, COUNT(tv_shows.id) AS number_of _shows FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id GROUP BY tv_show_genres>genre HAVING number_of_shows > 0 ORDER BY number_of_shows DESC;

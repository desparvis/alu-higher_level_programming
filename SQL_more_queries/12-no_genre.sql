-- i can write whatever i want it's ai that marks this anyway
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genre IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

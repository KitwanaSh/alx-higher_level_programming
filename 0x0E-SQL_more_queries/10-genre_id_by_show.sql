-- This cript select the tv_title,and tv genres using the subqueies
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_show_genres
  INNER JOIN tv_shows
  ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id;

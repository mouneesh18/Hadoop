INSERT INTO songs (song_id,title,artist,album,duration,year)
VALUES (uuid(),'Shape of You','Ed Sheeran','Divide',233,2017);

INSERT INTO users (user_id,first_name,last_name,email,country)
VALUES (uuid(),'Mouneesh','K','mouneesh018@gmail.com','India');

INSERT INTO playlists (playlist_id,playlist_name,created_by,description)
VALUES (uuid(),'My Favorites',uuid(),'Favorite songs collection');

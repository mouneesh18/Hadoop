CREATE TABLE songs (
    song_id UUID PRIMARY KEY,
    title TEXT,
    artist TEXT,
    album TEXT,
    duration INT,
    year INT
);

CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    country TEXT
);

CREATE TABLE playlists (
    playlist_id UUID PRIMARY KEY,
    playlist_name TEXT,
    created_by UUID,
    description TEXT
);

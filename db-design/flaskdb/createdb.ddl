ALTER USER postgres WITH PASSWORD 'c4cf7065b034787b2061088190bf737e';

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    username TEXT,
    email TEXT,
	age INTEGER
);

INSERT INTO students ( username, email, age )
VALUES ( 'Taro', 'taro@email.com', 20 );

INSERT INTO students ( username, email, age )
VALUES ( 'Jiro', 'jiro@email.com', 19 );

INSERT INTO students ( username, email, age )
VALUES ( 'Hanako', 'hanako@email.com', 18 );

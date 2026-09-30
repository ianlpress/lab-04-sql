CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(200),
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users VALUES (1, 'Alice', 'alice@email.com', 20);
INSERT INTO users VALUES (2, 'Bob', 'bob@email.com', 21);
INSERT INTO users VALUES (3, 'Charlie', 'charlie@email.com', 19);
INSERT INTO users VALUES (4, 'David', 'david@email.com', 22);
INSERT INTO users VALUES (5, 'Emma', 'emma@email.com', 20);
INSERT INTO users VALUES (6, 'Frank', 'frank@email.com', 23);
INSERT INTO users VALUES (7, 'Grace', 'grace@email.com', 21);
INSERT INTO users VALUES (8, 'Henry', 'henry@email.com', 20);
INSERT INTO users VALUES (9, 'Isabel', 'isabel@email.com', 22);
INSERT INTO users VALUES (10, 'Jack', 'jack@email.com', 19);

INSERT INTO posts VALUES (1, 1, 'Alice', 'Alice is cool');
INSERT INTO posts VALUES (2, 2, 'Soccer', 'Goal!');
INSERT INTO posts VALUES (3, 3, 'Dinosaurs', 'RAWRRRRR');
INSERT INTO posts VALUES (4, 4, 'Philosophy', 'What is the meaning of life?');
INSERT INTO posts VALUES (5, 5, 'UVA', 'Tech is nothing');
INSERT INTO posts VALUES (6, 6, 'Data Science', 'Numbers and coding and stuff');
INSERT INTO posts VALUES (7, 7, 'Adele', 'Hello, its me');
INSERT INTO posts VALUES (8, 8, 'Life is a highway', 'Im gonna ride it all night long');
INSERT INTO posts VALUES (9, 9, 'Black', 'Should never be worn with navy');
INSERT INTO posts VALUES (10, 10, 'Abercrombie', '& Fitch');

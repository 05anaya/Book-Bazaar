INSERT INTO books (id, author, price, minAge, maxAge, genres, series, `name`, `image`) VALUES
    (1, 'JK Rowling', 14, 12, NULL, 'Fantasy', 'Harry Potter', 'Harry Potter and the philosoper''s stone', 'https://images-na.ssl-images-amazon.com/images/I/5160dwNeqSL._SX323_BO1,204,203,200_.jpg'),
    (2, 'JK Rowling', 14, 12, NULL, 'Fantasy', 'Harry Potter', 'Harry Potter and the chamber of secrets', 'https://images-na.ssl-images-amazon.com/images/I/91go25u4pNL.jpg'),
    (3, 'JK Rowling', 14, 12, NULL, 'Fantasy', 'Harry Potter', 'Harry Potter and the prisoner of azkaban', 'https://images-na.ssl-images-amazon.com/images/I/81lAPl9Fl0L.jpg'),
    (4, 'JK Rowling', 14, 12, NULL, 'Fantasy', 'Harry Potter', 'Harry Potter and the the goblet of fire', 'https://images-na.ssl-images-amazon.com/images/I/81t2CVWEsUL.jpg'),
    (5, 'JK Rowling', 14, 12, NULL, 'Fantasy', 'Harry Potter', 'Harry Potter and the order of the pheonix', 'https://images-na.ssl-images-amazon.com/images/I/91t5-Juqt9L.jpg'),
    (6, 'JK Rowling', 14, 12, NULL, 'Fantasy', 'Harry Potter', 'Harry Potter and the half blood prince', 'https://images-na.ssl-images-amazon.com/images/I/915i0eI3J8L.jpg'),
    (7, 'JK Rowling', 14, 12, NULL, 'Fantasy', 'Harry Potter', 'Harry Potter and the deathly hallows', 'https://images-na.ssl-images-amazon.com/images/I/914CT7iyyvL.jpg'),
    (8,'Taylor Jenkins Reid',12,15,NULL,'romance',NULL,'The Seven Husbands of Evelyn Hugo','https://images-na.ssl-images-amazon.com/images/I/41FYr12RflL._SX320_BO1,204,203,200_.jpg'),
    (9,'Taylor Jenkins Reid',12,15,NULL,'romance',NULL,'Malibu rising','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzlC-GyWOZ72L6z0fk0k7oPwgLELqNAueAJPrI2eYuykq7l8z2bfKxHn7nYUS28IYZQo4&usqp=CAU'),
    (10,'Sally Thorne',11,14,NULL,'romance',NULL,'The Hating Game','https://images-na.ssl-images-amazon.com/images/I/917xGqEBBfL.jpg'),
    (11,'Sally Thorne',11,14,NULL,'romance',NULL,'99 percent mine','https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532485978l/36300625.jpg'),
    (12,'Collen Hoover',13,16,NULL,'romance',NULL,'ugly love','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_8yTKBzm2n83sa9DAJLJkyUZHcnPDN1ArgwdG34kGiSYojLOVG3zfDIdxowQA3W6y8ZE&usqp=CAU'),
    (13,'Collen Hoover',13,16,NULL,'thriller',NULL,'Verity','https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1634158558i/59344312._UY675_SS675_.jpg'),
    (14,'Paula Hawkins',12,16,NULL,'thriller',NULL,'Into the Waters','https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1523434763l/39752700.jpg'),
    (15,'Paula Hawkins',12,16,NULL,'thriller',NULL,'The girl on the train','https://upload.wikimedia.org/wikipedia/en/thumb/5/50/The_Girl_On_The_Train_%28US_cover_2015%29.png/220px-The_Girl_On_The_Train_%28US_cover_2015%29.png'),
    (16,'celcilia ahern',10,14,NULL,'dystopian','flawed','flawed','https://images-na.ssl-images-amazon.com/images/I/511Jj+oO3PL.jpg'),
    (17,'celcilia ahern',10,14,NULL,'dystopian','flawed','perfect','https://cclblog.files.wordpress.com/2018/01/perfect.jpg?w=584'),
    (18,'casey mcquinston',12,15,NULL,'romance',NULL,'Red ,white and Royal blue','https://images-na.ssl-images-amazon.com/images/I/71skR7IaVEL.jpg'),
    (19,'Amie Kaufman',12,12,NULL,'sci-fi','illuminae','Illuminae','https://images-na.ssl-images-amazon.com/images/I/51eHVZ-yB5L._SX329_BO1,204,203,200_.jpg'),
    (20,'Amie Kaufman',12,12,NULL,'sci-fi','illuminae','Gemina','https://images-na.ssl-images-amazon.com/images/I/91LeSmU+NQL.jpg'),
    (21,'Amie Kaufman',12,12,NULL,'sci-fi','illuminae','Obsidio','https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1501704611l/24909347.jpg');

CREATE TABLE users(
id INTEGER,
username TEXT NOT NULL,
hash TEXT NOT NULL,
address TEXT,
country TEXT,
state TEXT,
city TEXT,
PRIMARY KEy(id));

CREATE UNIQUE INDEX username ON users (username);

CREATE TABLE books(
id INTEGER,
author TEXT,
price NUMERIC,
minAge INTEGER,
maxAge INTEGER,
genres TEXT,
series TEXT, name TEXT, image text,
PRIMARY KEY(id));

CREATE TABLE order1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    order_num INTEGER,
    `time` TIMESTAMP,
   total_amt NUMERIC
   );
   
CREATE TABLE order_items(
id INTEGER,
order_id INTEGER,
book_id INTEGER,
qty INTEGER,
price NUMERIC,
PRIMARY KEY(id));

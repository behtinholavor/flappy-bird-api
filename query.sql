
DROP TABLE players;

CREATE TABLE players (
    id          INTEGER       PRIMARY KEY AUTOINCREMENT,
    name        VARCHAR (500) UNIQUE NOT NULL,
    big_score   INTEGER       DEFAULT (0),
    small_score INTEGER       DEFAULT (0),
    email       VARCHAR (500) UNIQUE DEFAULT (''),
    register    DATETIME      DEFAULT (CURRENT_TIMESTAMP) NOT NULL
);


--DELETE FROM players;

INSERT INTO players ( name, email) VALUES ('Jhon Doe', 'jhon_doe013@gmail.com');
INSERT INTO players ( name, email) VALUES ('Jack Jhonson', 'jack_jhonson87@gmail.com');
INSERT INTO players ( name, email) VALUES ('Alan More', 'jalan_more2@live.com');
INSERT INTO players ( name, email) VALUES ('Patrick Slave', 'patrick0193@yahoo.com');
INSERT INTO players ( name, email) VALUES ('Steve Loose', 'loose_stv184@.com');
INSERT INTO players ( name, email) VALUES ('Mary Jane', 'mary-jane813@gmail.com');
INSERT INTO players ( name, email) VALUES ('Mike Silver', 'mikesil_last@yahoo.com');
INSERT INTO players ( name, email) VALUES ('Aaron Nooby', 'aa-ron-nb@juker.com');
INSERT INTO players ( name, email) VALUES ('Sulivan Misty', 'sulivan0013@uol.com');
INSERT INTO players ( name, email) VALUES ('Carlson Guimmer', 'car-guimmer@globo.com');
INSERT INTO players ( name, email) VALUES ('Tayson Gray', 'gray.tay@yahoo.com');
INSERT INTO players ( name, email) VALUES ('Dana White', 'dana.w.80@live.com');
INSERT INTO players ( name, email) VALUES ('Yuri Glover', 'yuri-gl@dangerl.com');



SELECT * FROM players;
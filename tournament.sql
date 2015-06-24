-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table players(id serial, player_names text);
create table records(id int, wins int, matches int);

-- It is not necessery to create two tables because I think if table is created like 'create table games(id serial, player_names text, wins int, matches int)', 
-- it is in bcnf form and no multivaued dependency can be found in it. But due to deleteMatches and deletePlayers function, it looks reasonable to split it into two tables. 
#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        conn = psycopg2.connect("dbname=tournament")
        cursor = conn.cursor()
        return conn, cursor
    except:
        print ("Something wrong in connection")


def deleteMatches():
    """Remove all the match records from the database."""
    conn, cursor = connect()
    cursor.execute("TRUNCATE records")
    conn.commit()


def deletePlayers():
    """Remove all the player records from the database."""
    conn, cursor = connect()
    cursor.execute("TRUNCATE players")
    conn.commit()


def countPlayers():
    """Returns the number of players currently registered."""
    conn, cursor = connect()
    cursor.execute("SELECT coalesce (player_names, '0') from players")
    results = cursor.fetchall()
    if results == '0':
        return 0
    else:
        return len(results)


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    conn, cursor = connect()
    cursor.execute("INSERT into players(player_names) values (%s)", (name,))
    cursor.execute("SELECT id from players")
    results = cursor.fetchall()
    cursor.execute("INSERT into records values(%s, 0, 0)", (results[-1],))
    conn.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be
    the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, cursor = connect()
    cursor.execute("SELECT id, player_names, wins, matches "
                   "from players natural join records "
                   "order by wins desc")
    results = cursor.fetchall()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, cursor = connect()
    cursor.execute("UPDATE records "
                   "SET wins = wins + 1, matches = matches + 1 "
                   "where id = %s", (winner,))
    cursor.execute("UPDATE records "
                   "SET matches = matches + 1 "
                   "where id = %s", (loser,))
    conn.commit()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairs = []
    conn, cursor = connect()
    i, rank = 0, playerStandings()
    while i < len(rank):
        pairs.append((rank[i][0], rank[i][1], rank[i+1][0], rank[i+1][1]))
        i += 2
    return pairs

import sqlite3

# ---------------- CONNECT ----------------
def connect():
    return sqlite3.connect("fantasy.db")

# ---------------- CREATE TABLES ----------------
def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Players table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS players(
        name TEXT PRIMARY KEY,
        category TEXT,
        value INTEGER
    )
    """)

    # Teams table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS teams(
        team_name TEXT,
        player_name TEXT
    )
    """)

    # Match table (for score calculation)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS match(
        player TEXT,
        runs INTEGER,
        wickets INTEGER,
        catches INTEGER
    )
    """)

    conn.commit()
    conn.close()

# ---------------- INSERT PLAYERS ----------------
def insert_players():
    conn = connect()
    cur = conn.cursor()

    players = [
        ("Virat Kohli","BAT",100),
        ("Rohit Sharma","BAT",90),
        ("Shubman Gill","BAT",85),
        ("Shreyas Iyer","BAT",75),

        ("Jasprit Bumrah","BOWL",95),
        ("Mohammed Shami","BOWL",85),
        ("MD. Siraj","BOWL",60),
        

        ("Hardik Pandya","ALL",88),
        ("Ravindra Jadeja","ALL",85),
        ("Axar Patel","ALL",68),

        ("MS Dhoni","WK",80),
        ("KL Rahul","WK",85),
        ("Ishan Kishan","WK",70),
        ("Sanju Samson","WK",60)
    ]

    for p in players:
        try:
            cur.execute("INSERT INTO players VALUES (?,?,?)", p)
        except:
            pass

    conn.commit()
    conn.close()

# ---------------- INSERT MATCH DATA ----------------
def insert_match_data():
    conn = connect()
    cur = conn.cursor()

    # Clear old data
    cur.execute("DELETE FROM match")

    data = [
        ("Virat Kohli",100,0,1),
        ("Rohit Sharma",70,0,0),
        ("Shubman Gill",30,0,1),
        ("Shreyas Iyer",45,0,2),

        ("Jasprit Bumrah",5,3,0),
        ("Mohammed Shami",10,2,1),
        ("MD. Siraj",15,1,1),

        ("Hardik Pandya",40,1,1),
        ("Ravindra Jadeja",35,2,2),
        ("Axar Patel",25,3,1),

        ("MS Dhoni",20,0,2),
        ("KL Rahul",45,0,1),
        ("Ishan Kishan",55,0,0),
        ("Sanju Samson",12,0,0)
    ]

    for d in data:
        cur.execute("INSERT INTO match VALUES (?,?,?,?)", d)

    conn.commit()
    conn.close()
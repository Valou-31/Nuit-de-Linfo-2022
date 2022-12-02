import sqlite3
con = sqlite3.connect("bd.sqlite")
cur = con.cursor()

cur.execute("""
DROP TABLE CHANNEL
""")

cur.execute("""
DROP TABLE MSG
""")

con.commit()

cur.execute("""
CREATE TABLE channel(
id integer not null primary key autoincrement,
nom text not null)
""")

cur.execute("""
CREATE TABLE msg(
id integer not null primary key autoincrement,
msgContent text not null,
isAdmin integer not null,
channel_id integer not null)
""")

con.commit()

cur.execute("""
INSERT INTO channel(
    nom )VALUES('test1')
    """
)

cur.execute("""
INSERT INTO channel(
    nom )VALUES('test2')
    """
)

con.commit()

con.close()
import sqlite3

class BD:
    def __init__(self, path: str) -> None:
        self.__conn = sqlite3.connect(path)

    def getChannels(self):
        cur = self.__conn.cursor()
        cur.execute("""select nom,id from channel""")
        return cur.fetchall()

    def addChannel(self, name: str):
        cur = self.__conn.cursor()
        cur.execute(f"""insert into channel(nom) values("{name}")""")
        self.__conn.commit()

    def delChannel(self, id: int):
        cur = self.__conn.cursor()
        cur.execute(f"""delete from channel where id = {id}""")
        self.__conn.commit()

    def addMessage(self, msg_content: str, chan_id: int):
        cur = self.__conn.cursor()
        cur.execute(f"""insert into msg(msgContent,isAdmin,channel_id) values("{msg_content}",1,{chan_id})""")
        self.__conn.commit()
    
    def getMessages(self, chan_id: int, max: int):
        cur = self.__conn.cursor()
        cur.execute(f"""select msgContent, id from msg where channel_id = {chan_id} order by id DESC limit {max}""")
        return cur.fetchall()
    
    def delMessage(self, msg_id: int):
        cur = self.__conn.cursor()
        cur.execute(f"""delete from msg where id = {msg_id}""")
        self.__conn.commit()
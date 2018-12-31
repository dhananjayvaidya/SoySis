
#from ..database import db
import sqlite3
import json
class AppConfigService(object):
    def __init__(self):
        pass
    
    def setTwitterDetails(self,consumer_key,consumer_secret,access_token,access_token_secret):
        connection = sqlite3.connect("app.db")
        cur1 = connection.cursor()
        cur1.execute("INSERT INTO config (key_name,val) values('consumer_key','"+consumer_key+"'),('consumer_secret','"+consumer_secret+"'),('access_token','"+access_token+"'),('access_token_secret','"+access_token_secret+"')")
        connection.commit()
        connection.close()
        return True

    def getTwitterDetails(self):
        connection = sqlite3.connect("app.db")
        cur = connection.cursor()
        cur.execute("SELECT * FROM config WHERE key_name='consumer_key' OR key_name='consumer_secret' OR key_name='access_token' OR key_name='access_token_secret'")
        rows = cur.fetchall()
        connection.close()
        return json.dumps(rows)
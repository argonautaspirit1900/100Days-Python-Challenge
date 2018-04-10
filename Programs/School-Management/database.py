import sqlite3

class Manage:
	def __init__(self,fileLocation):
		self.fileLocation = fileLocation

	def connect(self):
		self.conn = sqlite3.connect(self.fileLocation)
		print("CONNECTED")

	def create_table(self,table):
		c = self.conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS ?(
			ID INTEGER,
			name TEXT,
			lastname TEXT,
			username TEXT UNIQUE,
			password TEXT)
			"""), table
		self.conn.commit()
	def insert(self,ID,name,lname,usern,passw):
		c = self.conn.cursor("INSERT INTO accounts VALUES(?,?,?,?)"), (ID,name,lname,usern,passw)
		c.execute()

	def getAccounts(table):
		c = self.conn.cursor()
		accounts = []
		for account in c.execute("FROM %s import *" % table):
			for item in range(4):
				accounts.insert(item)
		return accounts	
	

#dbManage = Manage("database-test")
#dbManage.connect()
#dbManage
import sqlite3

class Manage:
	def __init__(self,fileLocation):
		self.fileLocation = fileLocation

	def connect(self):
		self.conn = sqlite3.connect(self.fileLocation)
		print("CONNECTED")

	def create_table(self,table):
		c = self.conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS {}(
			ID INTEGER UNIQUE,
			name TEXT,
			lastname TEXT,
			username TEXT UNIQUE,
			password TEXT)
			""".format(table))
		self.conn.commit()
	def insert(self,table,ID,name,lname,usern,passw):
		c = self.conn.cursor()
		c.execute("INSERT INTO %s Values(%s,%s,%s,%s,%s)" % (table,ID,name,lname,usern,passw))
		#c.execute('INSERT INTO students Values(?,?,?,?,?)', (ID,name,lname,usern,passw))
		#c.execute("INSERT INTO {} Values({},{},{},{},{})".format(table,ID,name,lname,usern,passw))
		self.conn.commit()

	def getAccounts(self,table):
		c = self.conn.cursor()
		accounts = []
		accInfo = []
		for account in c.execute("SELECT * FROM {}".format(table)):
			print(account)
			for item in range(4):
				accInfo.append(account[item])
			accounts.append(accInfo)
			accInfo = []
		return accounts	
	

dbManage = Manage("database-test")
dbManage.connect()
dbManage.create_table("students")
#dbManage.insert("students","1","gjerg1j","kadriu","dsadas","gjergji")
acc = dbManage.getAccounts("students")
print(acc)
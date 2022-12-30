import mysql.connector

cnx = mysql.connector.connect(user='root', password='11megan11',
                              host='localhost',
                              database='api')
csr = cnx.cursor()

csr.execute("select stbrcd from wm370basd.ststyl00 where ststyl='DL48CART'")

result = csr.fetchone()


trim1 = result[0]
trim2 = trim1.strip()

print(trim2)

cnx.close()

import fdb

def getConnection():
    return fdb.connect(dsn='C:\Gplus\DADOS\GPLUS.FDB', user='sysdba', password='masterkey').cursor()
    
def getProduct():
    cur = getConnection()
    cur.execute("select * from PRODUTO")
    return cur.fetchall()

def getProductById(id):
    cur = getConnection()
    cur.execute("select * from PRODUTO where ID = {}".format(id))
    return cur.fetchall()

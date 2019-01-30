import MySQLdb

def connectDB():
    conn = MySQLdb.connect(
        host='localhost',
        user='uxfac',
        password='uxfac',
        db='wcgmanager',
        charset='utf8'
    )
    return conn
def insertTeamInfo(conn, teamName):
    with conn.cursor() as cursor:
        sql = 'INSERT INTO test (teamloginid, keyvalue) VALUES (%s, %s)'
        cursor.execute(sql, (teamName, teamName))
    conn.commit()
    print(cursor.lastrowid)

def insertKey(conn, teamName, key):
    with conn.cursor() as cursor:
        sql = 'INSERT INTO test (teamloginid, keyvalue) VALUES (%s, %s)'
        cursor.execute(sql, (teamName, teamName))
    conn.commit()
    print(cursor.lastrowid)

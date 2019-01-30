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

def insertKey(conn, teamName, MyKey):
    keyfingerprint = MyKey['KeyFingerprint']
    keymaterial = MyKey['KeyMaterial']
    keyname = MyKey['KeyName']

    with conn.cursor() as cursor:
        sql = 'UPDATE test SET keyname = %s, keyfingerprint = %s, keyvalue WHERE teamloginid = %s'
        cursor.execute(sql, (keyname, keyfingerprint, keymaterial))
    conn.commit()
    print(cursor.lastrowid)

def insertTest(conn, teamName):
    with conn.cursor() as cursor:
        sql = 'UPDATE test SET playercpuinstanceip = %s, playercpuinstanceid = %s WHERE teamloginid = %s'
        cursor.execute(sql, ('0.0.0.0', '1.1.1.1', teamName))
    conn.commit()
    print(cursor.lastrowid)
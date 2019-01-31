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
        sql = 'UPDATE test SET keyname = %s, keyfingerprint = %s, keyvalue = %s WHERE teamloginid = %s'
        cursor.execute(sql, (keyname, keyfingerprint, keymaterial, teamName))
    conn.commit()
    print(cursor.lastrowid)


def insertInstance(conn, teamName, instanceId, instanceIp):
    with conn.cursor() as cursor:
        sql = 'UPDATE test SET playercpuinstanceid = %s, playergpuinstanceid = %s, simulatorinstanceid = %s, playercpuinstanceip = %s, playergpuinstanceip = %s, simulatorinstanceip = %s  WHERE teamloginid = %s'
        cursor.execute(sql, (
        instanceId[0], instanceId[1], instanceId[2], instanceIp[0], instanceIp[1], instanceIp[2], teamName))
    conn.commit()
    print(cursor.lastrowid)


def insertTest(conn, teamName):
    with conn.cursor() as cursor:
        sql = 'UPDATE test SET playercpuinstanceip = %s, playercpuinstanceid = %s WHERE teamloginid = %s'
        cursor.execute(sql, ('0.0.0.0', '1.1.1.1', teamName))
    conn.commit()
    print(cursor.lastrowid)

def selectTeamInstance(conn, teamName):
    with conn.cursor(MySQLdb.cursors.DictCursor) as cursor:
        sql = 'Select * from test'
        cursor.execute(sql)
        rows = cursor.fetchall()
        instanceids = ['','','']
        for row in rows:
            instanceids[0] = row['playercpuinstanceid']
            instanceids[1] = row['playergpuinstanceid']
            instanceids[2] = row['simulatorinstanceid']

    return instanceids

def deleteTeamInfo(conn, teamName):
    with conn.cursor() as cursor:
        sql = 'DELETE FROM test WHERE teamloginid=%s'
        cursor.execute(sql, (teamName,))
    conn.commit()
    print(cursor.lastrowid)

def showDatabase(conn):
    with conn.cursor() as cursor:
        sql = 'Select * from test'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

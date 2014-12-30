__author__ = 'guyanhua'

import MySQLdb
try:
    conn= MySQLdb.connect(
        host='192.168.1.48',
        port = 3306,
        user='root',
        passwd='1234',
        db ='vmdai_1124',
        )
    cur=conn.cursor()
    aa = cur.execute('select * from user')
    print "a",aa
    info = cur.fetchmany(aa)
    print info
    for ii in info:
        print ii
    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])



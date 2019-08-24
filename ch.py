import cx_Oracle
con=cx_Oracle.connect('dummy/123@localhost')
cur=con.cursor()
j=input().split(' ')
for i in j:
    cur.execute('drop table '+i+' cascade constraints')
cur.close()
con.close()
import pymssql
import demjson

conn=pymssql.connect(host='192.168.1.254',user='Kates_system',password='Password123',database='Kates')
'''
如果和本机数据库交互，只需修改链接字符串
conn=pymssql.connect(host='.',database='Michael')
'''
cur=conn.cursor()

##cur.execute('select top 5 id,slavename,timeaddnew from S_SlaveIP')
cur.execute('select top 5 * from S_SlaveIP')
#如果update/delete/insert记得要conn.commit()
#否则数据库事务无法提交
##print (cur.fetchall())
##li = cur.fetchall()
##print (demjson.encode(li))


fo = open("foo.txt", "w")
li = cur.fetchall()
fo.write( "www.runoob.com!\nVery good site!\n")
fo.write(  demjson.encode(li))
# 关闭打开的文件
fo.close()

cur.close()

conn.close()

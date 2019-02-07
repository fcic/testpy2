import pymysql
def OpertionMysql(host,user,passwd,db,sql,port=3306,charset='utf8'):
    conn = pymysql.connect(
        host=host, # 连接的数据库服务器的主机名
        user=user, # 登录数据库的用户名
        passwd=passwd, # 登录数据库的密码
        port=port, # 端口号，MySQL 默认是3306
        db=db, # 要使用的数据库名
        charset=charset # 字符编码
    )#建立连接
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)# 建立游标  指针对象
    cur.execute(sql) # 执行sql ，执行单条sql语句，接手的参数为sql语句本身和使用的参数列表
    if sql.startswith('select'):#判断语句，如果是查询语句
        res  = cur.fetchone() # 接收返回值，接收一条返回结果
        # res  = cur.fetchall() # 接收全部的返回结果。返回结果集中的全部数据，结果为一个tuple的列表
    else: # 如果是增删改语句
        conn.commit() # 提交新增和修改
        res = 666
    cur.close() # 关闭游标
    conn.close() # 关闭数据库连接
    return res

if __name__ == '__main__':
    sql1 = 'insert into alina(id,username,password) value(98,"alina","123456")' # 新增
    sql2 = 'select * from tbl_books limit 3;' # 查询
    sql3 = 'delete from alina where id = 1;' # 删除
    sql4 = 'update alina set name = "hello" where id = 3;' # 修改
    s = OpertionMysql(
        host='192.168.1.254',user='root',passwd='n9u3y6bm',db='db_php_class',
        sql = sql2
)

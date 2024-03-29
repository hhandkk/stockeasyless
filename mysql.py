import pymysql
import config

def get_conn():
    return pymysql.connect(
        #host='112.74.98.79',
        #user='root',
        #password='abcd1234#',
        #database='myquote',
        #port=3306
        host = config.getConfig()["db"]["host"],
        user = config.getConfig()["db"]["user"],
        password = config.getConfig()["db"]["password"],
        database = config.getConfig()["db"]["database"],
        port = config.getConfig()["db"]["port"]
    )


def query_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()

def insert_or_update_data(sql, val):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, val)
        conn.commit()
    finally:
        conn.close()

def delete_data(sql, val):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, val)
        conn.commit()
    finally:
        conn.close()

def insert_data_bath(sql,obj):
    con = get_conn()
    try:
        # 创建游标对象
        with con.cursor() as cursor:
            # 批量插入
            cursor.executemany(sql, obj)
            # 提交事务
            con.commit()
    finally:
        # 关闭数据库连接
        con.close()
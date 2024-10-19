import pymysql

# 数据库连接参数
db_params = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'huitailang',
    'charset': 'utf8mb4'
}

# 连接数据库
connection = pymysql.connect(**db_params)

try:
    # 创建cursor对象
    with connection.cursor() as cursor:
        # 执行SQL语句
        sql = "drop database hui"
        cursor.execute(sql)

        # 获取查询结果
        results = cursor.fetchall()
        for row in results:
            print(row)
finally:
    # 关闭数据库连接
    connection.close()
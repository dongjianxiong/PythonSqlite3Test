
# coding=utf-8
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入SQLITE3模块
import sqlite3
import EMPloyee
# import pymysql

# SQLite数据库名
DB_SQLITE_NAME = "Company.db"
DB_EMPLOYEE_TABLE = "EMPLOYEE"


def sqliteHandler():
    '''''
    Author:Eric.Tang
    Date:2013-04-16
    Description:创建数据库表并插入测试数据
    '''

    str = input("请输入123：")
    print("你输入的内容是：", str)
    if str != "123":
        return

    # 连接数据库
    sqlite_conn = connectDB()

    # 如果存在表先删除
    # deleteTable(sqlite_conn, DB_EMPLOYEE_TABLE)

    # 创建表
    creatDbTable(sqlite_conn, DB_EMPLOYEE_TABLE)

    # 添加一条记录
    employeeUids = ["123","111","121","122","002","031"]
    for index, value in enumerate(employeeUids):
        employee = EMPloyee.Employee(value, "Lenny" + value, 29, 1, 'Beijing', 11111.00)
        insertEmplyee(sqlite_conn, employee)
        # selectEmployee(sqlite_conn, employee.uid)

    # 删除记录
    # deleteEmployee(sqlite_conn, employee.uid)

    # 查询记录
    selectAllEmployee(sqlite_conn)

def connectDB():
    try:
        sqlite_conn = sqlite3.connect(DB_SQLITE_NAME)
    except:
        return
    # except sqlite3.Error, e:
    #     print("连接sqlite3数据库失败", "\n", e.args[0])
    #     return
    return sqlite_conn

def deleteTable(sqlite_conn,tableName):
    # 获取游标
    sqlite_cursor = sqlite_conn.cursor()
    sql_del = "DROP TABLE IF EXISTS %s;" % (tableName)
    try:
        sqlite_cursor.execute(sql_del)
    except e:
        print("删除数据库表失败！", "\n", e.args[0])
        return
    sqlite_conn.commit()

def creatDbTable(sqlite_conn,tableName):

    sql_add = '''CREATE TABLE IF NOT EXISTS %s
           (UID            TEXT    NOT  NULL,
           NAME           TEXT    NOT  NULL,
           AGE            INT     NOT  NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL, PRIMARY KEY(UID, NAME));''' % (tableName)

    try:
        sqlite_conn.execute(sql_add)
    except e:
        print("创建数据库表失败haha！", "\n", e.args[0])
        return
        sqlite_conn.commit()


def insertEmplyee(sqlite_conn,employee):
    # 获取游标
    sqlite_cursor = sqlite_conn.cursor()
    try:
        insert_str = "INSERT OR REPLACE INTO %s (UID,NAME,AGE,ADDRESS,SALARY) \
              VALUES ('%s', '%s', %d, '%s', %.2f )" % (DB_EMPLOYEE_TABLE, employee.uid, employee.name, employee.age, employee.address, employee.salary)

        sqlite_cursor.execute(insert_str)
    #
    except e:
        print("添加数据失败！", "\n", e.args[0])
        return
    sqlite_conn.commit()


def selectEmployee(sqlite_conn,uid):
    # 获取游标
    sqlite_cursor = sqlite_conn.cursor()
    sql_select = "SELECT * FROM %s where UID='%s';" % (DB_EMPLOYEE_TABLE ,uid)
    sqlite_cursor.execute(sql_select)
    for row in sqlite_cursor:
        # i = 1;
        # print "数据表第%s" % i, "条记录是：", row,
        print("UID = ", row[0])
        print("NAME = ", row[1])
        print("AGE = ", row[2])
        print("ADDRESS = ", row[3])
        print("SALARY = ", row[4], "\n")


def deleteEmployee(sqlite_conn,uid):
    # 获取游标
    sqlite_cursor = sqlite_conn.cursor()
    sql_delete = "DELETE from %s where UID='%s';" % (DB_EMPLOYEE_TABLE ,uid)
    sqlite_cursor.execute(sql_delete)


def selectAllEmployee(sqlite_conn):
    # 获取游标
    sqlite_cursor = sqlite_conn.cursor()
    sql_select = "SELECT * FROM %s;" % (DB_EMPLOYEE_TABLE)
    sqlite_cursor.execute(sql_select)
    for row in sqlite_cursor:
        i = 1
        print("数据表第%s" % i, "条记录是：", row, "\n",)



if __name__ == '__main__':
    # 调用数据库操作方法
    sqliteHandler()


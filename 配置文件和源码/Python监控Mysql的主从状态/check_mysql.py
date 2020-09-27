# coding:utf-8
import pymysql
import sys
class Check_mysql_repl():
    def __init__(self):
        self.host= "192.168.106.161"
        self.user="monitor"
        self.password="monitor"
        self.database= "test"
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.sql="show slave status"
        self.cursor.execute(self.sql)
        self.data= self.cursor.fetchall()
        self.io  = self.data[0]['Slave_IO_Running']
        self.sql = self.data[0]['Slave_SQL_Running']
        self.time = self.data[0]['Seconds_Behind_Master']
        self.conn.close()

    def get_io_status(self):
        if self.io == 'Yes':
            return 1
        else:
            return 0

    def get_sql_status(self):
        if self.sql == 'Yes':
            return 1
        else:
            return 0

if __name__ == '__main__':
    mysql_db = Check_mysql_repl()
    if len(sys.argv) != 2:
        try:
            print("Usages:%s [io|sql|time]") % sys.argv[0]
        except:
            pass

    if sys.argv[1] =='io':
        print(mysql_db.get_io_status())
    elif sys.argv[1] == 'sql':
        print(mysql_db.get_sql_status())
    elif sys.argv[1] == 'time':
        print(mysql_db.time)
    else:
        print("it have no such argvs!")
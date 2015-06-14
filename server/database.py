#coding=utf-8

import mysql.connector


class MySqlDB:
    #数据库连接类，连接并建立到mysql的查询关系，方便程序中使用
    def __init__(self):
        self._config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'port': 3306,
            'database': 'hotel',
            'charset': 'utf8'
        }

        try:
            self._conn = mysql.connector.connect(**self._config)
        except mysql.connector.Error as e:
            print 'MySQL connect fails{}'.format(e)

    def insert_user(self, item):
        cursor = self._conn.cursor()
        try:
            sql = "insert into user(room_id, name, check_in) values \
                (%s, %s, %s);" % item
            cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('insert error!{}'.format(e))
        finally:
            cursor.close()

    def insert_client(self, item):
        cursor = self._conn.cursor()
        try:
            sql = "insert into client(room_id ,state, targetTemp, fanLevel, curTemp, cost)\
                values ('%s', '%s', %s, %s, %s, %s);" % item
            #print sql
            cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('insert error!{}'.format(e))
        finally:
            cursor.close()

    def insert_list(self, item):
        cursor = self._conn.cursor()
        try:
            sql = "insert into list(room_id ,beginTime, endTime, state, fanLevel, \
                beginTemp, endTemp, cost) values ('%s', '%s', '%s', '%s', \
                %s, %s, %s, %s);" % item
            #print "- [database] <sql> insert list", sql
            cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('insert error!{}'.format(e))
        finally:
            cursor.close()

    def update_client_query(self, item):
        cursor = self._conn.cursor()
        try:
            sql = "update client set state='%s', targetTemp='%s', fanLevel='%s' \
                where room_id='%s';" % item
            #print "- [database] <sql> update client query ", sql
            cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('update error!{}'.format(e))
        finally:
            cursor.close()

    def update_client_result(self, item):
        cursor = self._conn.cursor()
        try:
            sql = "update client set curTemp='%s', cost='%s' \
                where room_id='%s';" % item
            #print "- [database] <sql> update client result ", sql
            cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('update error!{}'.format(e))
        finally:
            cursor.close()

    def update_client_curtemp(self, item):
        cursor = self._conn.cursor()
        try:
            sql = "update client set curTemp='%s' where room_id='%s';" % item
            #print "- [database] <sql> update client curtemp ", sql
            cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('update error!{}'.format(e))
        finally:
            cursor.close()

    def update_list(self, item):
        cursor = self._conn.cursor()
        try:
            sql = "update list set endTime='%s', endTemp='%s' \
                where room_id='%s';" % item
            #print sql
            cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('update error!{}'.format(e))
        finally:
            cursor.close()

    def query_user_room(self):
        cursor = self._conn.cursor()
        try:
            sql = "select room_id from user;"
            cursor.execute(sql)
            res = []
            for item in cursor:
                res.append(item)
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            return res

    def query_user(self, room_id):
        cursor = self._conn.cursor()
        try:
            sql = "select * from user where room_id='%s';" % room_id
            cursor.execute(sql)
            res = {}
            for room_id, name, check_in in cursor:
                res['room_id'] = room_id
                res['name'] = name
                res['check_in'] = check_in
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            return res

    def query_client(self, room_id):
        cursor = self._conn.cursor()
        try:
            sql = "select * from client where room_id='%s';" % room_id
            #print sql
            cursor.execute(sql)
            res = {}
            for room_id, state, targetTemp, fanLevel, curTemp, cost in cursor:
                #print room_id
                res['room_id'] = room_id
                res['state'] = state
                res['targetTemp'] = targetTemp
                res['fanLevel'] = fanLevel
                res['curTemp'] = curTemp
                res['cost'] = cost

        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            #print res
            return res

    def query_list(self, room_id):
        cursor = self._conn.cursor()
        try:
            sql = "select * from list where room_id='%s';" % room_id
            cursor.execute(sql)
            res = []
            item = {}
            for room_id, beginTime, endTime, state, fanLevel, beginTemp, \
                endTemp, cost in cursor:
                res.append([room_id, beginTime, endTime, state, fanLevel, \
                    beginTemp, endTemp, cost])
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            return res


    def query_list_sum(self, room_id):
        cursor = self._conn.cursor()
        try:
            sql = "select sum(cost) from list where room_id=%s;" % room_id
            cursor.execute(sql)

            for cost in cursor:
                res = cost
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            return res


    def delete_user(self, room_id):
        cursor = self._conn.cursor()
        try:
            sql = "delete from user where room_id='%s';"
            cursor.execute(sql, room_id)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('delete error!{}'.format(e))
        finally:
            cursor.close()

    def delete_client(self, room_id):
        cursor = self._conn.cursor()
        try:
            sql = "delete from client where room_id='%s';"
            cursor.execute(sql, room_id)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('delete error!{}'.format(e))
        finally:
            cursor.close()

    def delete_list(self, room_id):
        cursor = self._conn.cursor()
        try:
            sql = "delete from list where room_id='%s';"
            cursor.execute(sql, room_id)
            self._conn.commit()
        except mysql.connector.Error as e:
            print('delete error!{}'.format(e))
        finally:
            cursor.close()

    def close(self):
        self._conn.close()


if __name__ == '__main__':
    db = MySqlDB()
    db.insert()
    db.close()

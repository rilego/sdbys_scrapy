import mysql.connector
from sdbys import settings

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='sdbys')
cur = cnx.cursor(buffered=True)


class Sql:
    @classmethod
    def insert_sdbys(cls, name, xueli, zhuanye, school, year, sex, time, guid):
        sql = 'insert into sdbys_tb1(name, degree, specialty, school, graduation, sex, posttime, guid) values(%(name)s, %(xueli)s, %(zhuanye)s, %(school)s, %(year)s, %(sex)s, %(time)s, %(guid)s)'
        value = {
            'name': name,
            'xueli': xueli,
            'zhuanye': zhuanye,
            'school': school,
            'year': year,
            'sex': sex,
            'time': time,
            'guid': guid
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_guid(cls, guid):
        sql = "select exists(select 1 from sdbys_tb1 where guid=%(guid)s)"
        value = {
            'guid': guid
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

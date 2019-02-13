# import pymysql
# from twisted.enterprise import adbapi
# from pymysql import cursors
#
# class JobboleTwistedPipeline(object):
#     def __init__(self):
#         dbparams = {
#             'host': '127.0.0.1',
#             'port': 3306,
#             'user': 'root',
#             'password': '123456',
#             'database': 'jobbole',
#             'charset': 'utf8',
#             'cursorclass': cursors.DictCursor
#         }
#         self.dbpool = adbapi.ConnectionPool("pymysql", **dbparams)
#         self._sql = None
#
#     @property
#     def sql(self):
#         if not self._sql:
#             self._sql = """
#                             insert into article(id,publish_time,category,content,title,origin_link,origin_author) values(null,%s,%s,%s,%s,%s,%s,)
#                         """
#             return self._sql
#         return self._sql
#
#     def process_item(self, item, spider):
#         defer = self.dbpool.runInteraction(self.insert_item, item)
#         defer.addErrback(self.handle_error, item, spider)
#
#     def insert_item(self, cursor, item):
#         cursor.execute(self.sql, (item['title'], item['content'], item['category'], item['origin_link'],
#                                   item['publish_time'],  item['origin_author'], ))
#
#     def handle_error(self, error, item, spider):
#         print('==='*10)
#         print(error)
#         print('==='*10)

import pymysql

class JobbolePipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jobbole',
            'charset': 'utf8',
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['content'], item['category'], item['origin_link'],
                                       item['origin_author'], item['publish_time']))

        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                        insert into article(id,title,content,category,origin_link,origin_author,publish_time) values (null,%s,%s,%s,%s,%s,%s)
                        """
            return self._sql
        return self._sql


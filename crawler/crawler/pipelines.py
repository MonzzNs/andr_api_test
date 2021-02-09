# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from main.models import Post
import mysql.connector

class CrawlerPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='test'
        )
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS post""")
        self.curr.execute("""create table post(
                        title text,
                        cover text,
                        rating text,
                        genres text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        
        self.curr.execute("""insert into post values (%s, %s, %s, %s)""", (
            item['title'][0],
            item['cover'][0],
            item['rating'][0],
            item['genres'][0]

        ))
        self.conn.commit()
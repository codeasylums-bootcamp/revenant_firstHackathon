# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class FlipkartPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("shopdata.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS inventory""")
        self.curr.execute("""create table inventory(
                        prod_brand text,
                        prod_name text,
                        prod_price text,
                        prod_discount text
                        )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline :" + item['prod_name'])
        return item
    
    def store_db(self,item):
        self.curr.execute("""insert into inventory values (?,?,?,?)""",(
            item['prod_brand'],
            item['prod_name'],
            item['prod_price'],
            item['prod_discount']
        ))
        self.conn.commit()
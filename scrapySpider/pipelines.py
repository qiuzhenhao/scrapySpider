# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 此文件为爬取之后item的数据处理页面，需要先在settings页面进行注册ITEM_PIPELINES
import json

class ScrapyspiderPipeline(object):
    def __init__(self):
        self.count = 0
        # 打开文件
        self.file = open('data.json', 'w', encoding='utf-8')
        self.db = pymysql.connect('localhost', 'root', '123456', 'tptest', use_unicode=True, charset="utf8")
        self.cursor = self.db.cursor()

    # 该方法用于处理数据
    def process_item(self, item, spider):

        # 将返回的Item插入数据库
        sql = "insert into imoocSpider(TITLE, LABEL, URL, IMAGE_URL, LEVEL, STUDENT_COUNT, INTRODUCTION)\
               VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
               % (item['title'], item['label'], item['url'], item['image_url'], item['level'], item['student_count'],
               item['introduction'])
        try:
            self.cursor.execute(sql)
            self.count = self.count + 1
            print("链接: %d" % self.count)
            self.db.commit()
        except:
            self.db.rollback()

        # # 读取item中的数据
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # # 写入文件
        # self.file.write(line)
        # # 返回item
        # return item

    # 该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    # 该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass
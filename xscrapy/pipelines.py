# -*- coding: utf-8 -*-

import codecs
import json
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XscrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    """
    使用自定义的类 JsonWithEncodingPipeline 将 item 保存到本地文件中
    """
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()

class JsonExporterPipeline(object):
    """
    使用 scrapy 提供的 JsonExporter 导出 Item 为 JSON 文件。
    """
    def __init__(self):
        self.file = open('article_exporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

class MysqlPipeline(object):

    def __init__(self):
        mysql_info = dict(
            host='127.0.0.1',
            user='root',
            password='19940423',
            port=3306,
            database='xscrapy',
            charset='utf8',
            use_unicode=True
        )
        self.conn = MySQLdb.connect(**mysql_info)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        """
            执行 MySQL 数据插入操作
        :param item:
        :param spider:
        :return:
        """
        insert_sql = """
            insert into article(title, url, url_object_id, date, content, image_url, image_path, tags, admiration_num, 
            collection_num, comment_num) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
        """
        try:
            self.cursor.execute(insert_sql % (item['title'], item['url'], item['url_object_id'],
                    item['date'].strftime('%Y-%m-%d'), item['content'], item['image_url'][0],
                    item['image_path'], item['tags'], item['admiration_num'], item['collection_num'], item['comment_num']))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        return item

class MysqlTwistedPipeline(object):
    """
    基于 Twisted 框架异步处理 MySQL 数据库操作
    """

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        """
            从 settings.py 中获取 MySQL 数据库配置
        :param settings:
        :return:
        """
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            database=settings['MYSQL_DATABASE'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        """
            使用 Twisted 将 MySQL 插入数据操作异步执行
        :param item:
        :param spider:
        :return:
        """
        # 第一个参数为异步执行的函数，第二个为该函数的参数
        insert = self.dbpool.runInteraction(self.do_insert, item)
        # 错误处理
        insert.addErrback(self.handle_error)

    def handle_error(self, error):
        """
            错误处理函数
        :param error:
        :return:
        """
        print(error)

    def do_insert(self, cursor, item):
        """
            执行 MySQL 数据插入操作
        :param cursor:
        :param item:
        :return:
        """
        insert_sql = """
                    insert into article(title, url, url_object_id, date, content, image_url, image_path, tags, admiration_num, 
                    collection_num, comment_num) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
        """
        try:
            cursor.execute(insert_sql % (item['title'], item['url'], item['url_object_id'],
                item['date'].strftime('%Y-%m-%d'), item['content'], item['image_url'][0], item['image_path'],
                item['tags'], item['admiration_num'], item['collection_num'], item['comment_num']))
        except Exception as e:
            print(e)




class ArticleImagePipeline(ImagesPipeline):

    def item_completed(self, results, item, info):
        """
        重写 ImagesPipeline 的 item_completed() 方法，获取图片的本地存放路径
        :param results:
        :param item:
        :param info:
        :return:
        """
        if 'image_path' in item:
            for flag, element in results:
                if flag:
                    item['image_path'] = element['path']
                else:
                    item['image_path'] = ''
        # 返回 item，供其他 Pipeline 使用
        return item


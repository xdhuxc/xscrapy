# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import Join

"""
Item 是用来保存爬取到的数据的容器，其使用方法和字典类似，也可以在 Scrapy 中直接使用字典，但是 Item 提供了额外的保护机制来避免拼写错误导致的未定义字段错误。
"""

def str2date(value):
    """
        将日期字符串转换为 date 类型
    :param value:
    :return:
    """
    try:
        date = datetime.datetime.strptime(value, '%Y/%m/%d')
    except Exception as e:
        date = datetime.datetime.now().date()
    return date

def get_nums_from_str(value):
    """
        使用正则表达式匹配出点赞数、收藏数、评论数等。
    :param value:
    :return:
    """
    regular_expression = '.*?(\d+).*'
    match_re = re.match(regular_expression, value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        # 如果没有收藏数，则将收藏数置为 0
        nums = 0
    return nums

def remove_tags_comment(value):
    """
        去除 tags 中的 “评论”
    :param value:
    :return:
    """
    if '评论' in value:
        return ''
    else:
        return value

class XscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()


class ArticleItemLoader(ItemLoader):
    """
        自定义 ItemLoader
    """
    # 为每一个字段都指定一个 output_processor
    default_output_processor = TakeFirst()


class JobboleArticle(scrapy.Item):
    """
        博客的 Item
    """
    title = scrapy.Field()
    url = scrapy.Field()
    # 做 MD5，变成一个长度固定的值
    url_object_id = scrapy.Field()
    date = scrapy.Field(
        input_processor=MapCompose(str2date)
    )
    content = scrapy.Field()
    image_url = scrapy.Field(
        # 需要的就是 List 形式的图片路径
        output_processor=MapCompose(lambda x: x)
    )
    image_path = scrapy.Field()
    tags = scrapy.Field(
        input_processor = MapCompose(remove_tags_comment),
        # 会覆盖掉 default_output_processor
        output_processor = Join(',')
    )
    admiration_num = scrapy.Field(
        input_processor=MapCompose(get_nums_from_str)
    )
    collection_num = scrapy.Field(
        input_processor=MapCompose(get_nums_from_str)
    )
    comment_num = scrapy.Field(
        input_processor=MapCompose(get_nums_from_str)
    )



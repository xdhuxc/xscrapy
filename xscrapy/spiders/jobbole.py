# -*- coding: utf-8 -*-

import re
import datetime
import scrapy

from scrapy.http import Request
from scrapy.loader import ItemLoader
from xscrapy.items import ArticleItemLoader
from urllib import parse

from ..items import JobboleArticle

from xscrapy.utils.common import get_md5

class JobboleSpider(scrapy.Spider):
    # 此名字必须是唯一的，用于区别 spider。
    name = 'jobbole'

    allowed_domains = ['blog.jobbole.com']
    # 包含了 spider 在启动时进行爬取的 url 列表，因此，第一个被获取到的页面将是其中之一。
    """
    scrapy 为 spider 的 start_urls 属性中的每个 URL 创建了 scrapy.Request 对象，并将 parse 方法作为 回调函数赋值给了 Request。
    Request 对象经过调度，执行生成 scrapy.http.Response 对象并送回给 spider 的 parse() 方法。
    """
    start_urls = ['http://blog.jobbole.com/all-posts/']


    def parse_details(self, response):
        """
            解析 response 中的各字段
        :param response:
        :return:
        """

        """
        article = JobboleArticle()
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        url = response.url
        date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first().strip().replace("·", "").strip()
        content = response.xpath('//div[@class="entry"]').extract_first()
        tags_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # 去除标签中的评论部分
        selected_tags = [item for item in tags_list if not item.endswith("评论 ")]
        tags = ",".join(selected_tags)
        image_url = response.meta.get('image_url', '')

        # class 属性中包含 vote-post-up 的元素
        admiration_num = int(response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract_first())
        
        # 使用正则表达式提取收藏数和点赞数
        # collection_num = int(response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract()[0].replace("收藏","").strip())
        collection_result = response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract_first()
        regular_expression = '.*?(\d+).*'
        match_re = re.match(regular_expression, collection_result)
        if match_re:
            collection_num = int(match_re.group(1))
        else:
            # 如果没有收藏数，则将收藏数置为 0
            collection_num = 0
        # comment_num = int(response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0].replace("评论","").strip())
        comment_result = response.xpath('//a[@href="#article-comment"]/span/text()').extract_first()
        match_re = re.match(regular_expression, comment_result)
        if match_re:
            comment_num = int(match_re.group(1))
        else:
            # 如果没有评论，则将评论数置为 0
            comment_num = 0

        article['title'] = title
        article['url'] = url
        article['url_object_id'] = get_md5(url)

        try:
            date = datetime.datetime.strptime(date, '%Y/%m/%d')
        except Exception as e:
            date = datetime.datetime.now().date()

        article['date'] = date
        article['content'] = content
        article['tags'] = tags
        article['image_url'] = [image_url, ]
        article['admiration_num'] = admiration_num
        article['collection_num'] = collection_num
        article['comment_num'] = comment_num
        """

        """
            基于 CSS 选择器来获取博客信息

        title = response.css('div[class="entry-header"] h1::text').extract_first()
        url = response.url
        date = response.css('p[class="entry-meta-hide-on-mobile"] ::text').extract_first().strip().replace('·', '').strip()
        body = response.css('div[class="entry"]').extract_first()
        tags_list = response.css('p[class="entry-meta-hide-on-mobile"] a::text').extract()
        selected_tags = [element for element in tags_list if not element.endswith('评论 ')]
        tags = ",".join(selected_tags)
        admiration_num = int(response.css('span[class~="vote-post-up"] h10::text').extract_first())

        collection_result = response.css('span[class~="bookmark-btn"] ::text').extract_first()
        regular_expression = ".*?(\d+).*"
        match_re = re.match(regular_expression, collection_result)
        if match_re:
            collection_num = int(match_re.group(1))
        comment_result = response.css('a[href="#article-comment"] ::text').extract_first()
        match_re = re.match(regular_expression, comment_result)
        if match_re:
            comment_num = int(match_re.group(1))
        """
        image_url = response.meta.get('image_url', '')
        # 通过 ItemLoader 加载 item
        item_loader = ArticleItemLoader(item=JobboleArticle(), response=response)
        item_loader.add_css('title', 'div[class="entry-header"] h1::text')
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id', get_md5(response.url))
        item_loader.add_css('date', 'p[class="entry-meta-hide-on-mobile"] ::text')
        item_loader.add_css('content', 'div[class="entry"]')
        item_loader.add_value('image_url', [image_url, ])
        item_loader.add_css('tags', 'p[class="entry-meta-hide-on-mobile"] a::text')
        item_loader.add_css('admiration_num', 'span[class~="vote-post-up"] h10::text')
        item_loader.add_css('collection_num', 'span[class~="bookmark-btn"] ::text')
        item_loader.add_css('comment_num', 'a[href="#article-comment"] ::text')

        article = item_loader.load_item()

        # yield 之后，article 将被传入 pipelines.py 中
        yield article

    def parse(self, response):
        """
        是 spider 的一个方法，被调用时，每个初始 URL 完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
        该方法负责解析返回的数据，提取数据（生成item）以及生成需要进一步处理的 URL 的 Request 对象。
        :param response:
        :return:
        """
        """
            1、获取文章列表页中文章的 url并交给 scrapy 下载，并进行解析。
            2、获取下一页的 url 并交给 scrapy 进行下载，下载完后交给 parse。
        """

        # 获取文章列表页中文章的 url并交给 scrapy 下载，并进行解析。
        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            # 文章的封面图片 url
            image_url = post_node.css('img::attr("src")').extract_first('')
            post_url = post_node.css('::attr("href")').extract_first('')

            """
            需要处理某些相对 url 没有域名的问题，使用 parse.urljoin() 方法。
            通过 meta 字典，可以向 response 传递数据。
            """
            yield Request(url=parse.urljoin(response.url, post_url), meta={"image_url": image_url}, callback=self.parse_details)

        # 获取下一页的 url 并交给 scrapy 进行下载，下载完后交给 parse。
        next_url = response.css('.next.page-numbers ::attr(href)').extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
















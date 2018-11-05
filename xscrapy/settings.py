# -*- coding: utf-8 -*-

import os

# Scrapy settings for xscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xscrapy'

SPIDER_MODULES = ['xscrapy.spiders']
NEWSPIDER_MODULE = 'xscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xscrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules，遵循 robots.txt 规则，将会导致我们只能爬取到网站指定的内容，所以设置为 False
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xscrapy.middlewares.XscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xscrapy.middlewares.XscrapyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 数据所流经的Pipeline，后面的数值表示优先级，数值越小，优先级越高。
ITEM_PIPELINES = {
    # 'xscrapy.pipelines.XscrapyPipeline': 300,
    # 'scrapy.pipelines.images.ImagesPipeline': 200
    # 'xscrapy.pipelines.JsonWithEncodingPipeline': 2,
    # 'xscrapy.pipelines.JsonExporterPipeline': 3,
    # 使用自定义的 ArticleImagePipeline
    'xscrapy.pipelines.ArticleImagePipeline': 1,
    #'xscrapy.pipelines.MysqlPipeline': 2
    'xscrapy.pipelines.MysqlTwistedPipeline': 2
}

# 定义下载的图片路径的字段
IMAGES_URLS_FIELD = 'image_url'

# 设置下载后的图片的存储路径
project_dir = os.path.abspath(os.path.dirname(__file__))

IMAGES_STORE = os.path.join(project_dir, 'images')


# 设置下载的图片的最小尺寸
# IMAGES_MIN_HEIGHT = 100
# IMAGES_MIN_WIDTH = 100


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 设置 MySQL 数据库连接信息
MYSQL_HOST='127.0.0.1'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASSWORD='19940423'
MYSQL_DATABASE='xscrapy'


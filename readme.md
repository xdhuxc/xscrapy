### 命令
1、创建工程
```angularjs
scrapy startproject
```
2、创建一个爬虫器
```angularjs
scrapy genspider jobbole blog.jobbole.com
```
3、运行 scrapy 
```angularjs
scrapy crawl jobbole
```
4、爬取页面
```angularjs
(xscrapy37) E:\PycharmProject\xscrapy>scrapy shell "http://blog.jobbole.com/all-posts/"
2018-10-19 17:20:02 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: xscrapy)
2018-10-19 17:20:02 [scrapy.utils.log] INFO: Versions: lxml 4.2.5.0, libxml2 2.9.5, cssselect 1.0.3, parsel 1.
5.0, w3lib 1.19.0, Twisted 18.9.0, Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit
(AMD64)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0i  14 Aug 2018), cryptography 2.3.1, Platform Windows-10-10.0.17134-S
P0
2018-10-19 17:20:02 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'xscrapy', 'DUPEFILTER_CLASS': 's
crapy.dupefilters.BaseDupeFilter', 'LOGSTATS_INTERVAL': 0, 'NEWSPIDER_MODULE': 'xscrapy.spiders', 'SPIDER_MODU
LES': ['xscrapy.spiders']}
2018-10-19 17:20:02 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole']
2018-10-19 17:20:03 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2018-10-19 17:20:03 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2018-10-19 17:20:03 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-10-19 17:20:03 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2018-10-19 17:20:03 [scrapy.core.engine] INFO: Spider opened
2018-10-19 17:20:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://blog.jobbole.com/all-posts/> (refere
r: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x00000203F6E18978>
[s]   item       {}
[s]   request    <GET http://blog.jobbole.com/all-posts/>
[s]   response   <200 http://blog.jobbole.com/all-posts/>
[s]   settings   <scrapy.settings.Settings object at 0x00000203F6E18B38>
[s]   spider     <JobboleSpider 'jobbole' at 0x203f70c1978>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
In [1]: response.xpath('//title')
Out[1]: [<Selector xpath='//title' data='<title>所有文章 - 文章 - 伯乐在线</title>'>]

In [2]: response.xpath('//title').extract()
Out[2]: ['<title>所有文章 - 文章 - 伯乐在线</title>']

In [3]: response.xpath('//title/text()').extract()
Out[3]: ['所有文章 - 文章 - 伯乐在线']

```


### 常见问题及解决
1、安装 scrapy 时，报错如下：
```angularjs
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/

----------------------------------------
Command "e:\pycharmproject\envs\xscrapy\scripts\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\wanghuan\\AppData\\Local\\Temp\\pip-install-83srp8ht\\Twisted\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\wanghuan\AppData\Local\Temp\pip-record-zaulcand\install-record.txt --single-version-externally-managed --compile --install-headers e:\pycharmproject\envs\xscrapy\include\site\python3.7\Twisted" failed with error code 1 in C:\Users\wanghuan\AppData\Local\Temp\pip-install-83srp8ht\Twisted\
```
到 https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted 上，下载对应版本的 Twisted-18.7.0-cp37-cp37m-win32.whl，然后安装之。
```angularjs
pip install C:\Users\wanghuan\Downloads\Twisted-18.7.0-cp37-cp37m-win32.whl
或者
pip install https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/Twisted-18.9.0-cp35-cp35m-win_amd64.whl
```
然后继续安装 scrapy 即可。

2、执行 `scrapy crawl jobbole` 时，报错如下：
```angularjs
(venv) E:\PycharmProject\xscrapy>scrapy crawl jobbole
2018-10-17 07:49:50 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: xscrapy)
2018-10-17 07:49:50 [scrapy.utils.log] INFO: Versions: lxml 4.2.5.0, libxml2 2.9.5, cssselect 1.0.3, parsel 1.5.0, w3lib 1.19.0, Twisted 18.7.0, Python 2.7.14 (v2.7.14:84471935ed, S
ep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0i  14 Aug 2018), cryptography 2.3.1, Platform Windows-10-10.0.17134
2018-10-17 07:49:50 [scrapy.crawler] INFO: Overridden settings: {'NEWSPIDER_MODULE': 'xscrapy.spiders', 'SPIDER_MODULES': ['xscrapy.spiders'], 'ROBOTSTXT_OBEY': True, 'BOT_NAME': 'x
scrapy'}
2018-10-17 07:49:50 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.logstats.LogStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.corestats.CoreStats']
Unhandled error in Deferred:
2018-10-17 07:49:50 [twisted] CRITICAL: Unhandled error in Deferred:

2018-10-17 07:49:50 [twisted] CRITICAL:
Traceback (most recent call last):
  File "c:\xdhuxc\python\lib\site-packages\twisted\internet\defer.py", line 1418, in _inlineCallbacks
    result = g.send(result)
  File "c:\xdhuxc\python\lib\site-packages\scrapy\crawler.py", line 98, in crawl
    six.reraise(*exc_info)
  File "c:\xdhuxc\python\lib\site-packages\scrapy\crawler.py", line 80, in crawl
    self.engine = self._create_engine()
  File "c:\xdhuxc\python\lib\site-packages\scrapy\crawler.py", line 105, in _create_engine
    return ExecutionEngine(self, lambda _: self.stop())
  File "c:\xdhuxc\python\lib\site-packages\scrapy\core\engine.py", line 69, in __init__
    self.downloader = downloader_cls(crawler)
  File "c:\xdhuxc\python\lib\site-packages\scrapy\core\downloader\__init__.py", line 88, in __init__
    self.middleware = DownloaderMiddlewareManager.from_crawler(crawler)
  File "c:\xdhuxc\python\lib\site-packages\scrapy\middleware.py", line 58, in from_crawler
    return cls.from_settings(crawler.settings, crawler)
  File "c:\xdhuxc\python\lib\site-packages\scrapy\middleware.py", line 34, in from_settings
    mwcls = load_object(clspath)
  File "c:\xdhuxc\python\lib\site-packages\scrapy\utils\misc.py", line 44, in load_object
    mod = import_module(module)
  File "c:\xdhuxc\python\lib\importlib\__init__.py", line 37, in import_module
    __import__(name)
  File "c:\xdhuxc\python\lib\site-packages\scrapy\downloadermiddlewares\retry.py", line 20, in <module>
    from twisted.web.client import ResponseFailed
  File "c:\xdhuxc\python\lib\site-packages\twisted\web\client.py", line 41, in <module>
    from twisted.internet.endpoints import HostnameEndpoint, wrapClientTLS
  File "c:\xdhuxc\python\lib\site-packages\twisted\internet\endpoints.py", line 41, in <module>
    from twisted.internet.stdio import StandardIO, PipeAddress
  File "c:\xdhuxc\python\lib\site-packages\twisted\internet\stdio.py", line 30, in <module>
    from twisted.internet import _win32stdio
  File "c:\xdhuxc\python\lib\site-packages\twisted\internet\_win32stdio.py", line 9, in <module>
    import win32api
ImportError: No module named win32api

```
解决：使用 pip 安装 pypiwin32，命令如下：
```angularjs
pip install pypiwin32
```

### 参考资料

https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html
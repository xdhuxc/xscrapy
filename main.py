#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wanghuan
# date: 2018-10-17
# description:

from scrapy import cmdline

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

cmdline.execute(argv=['scrapy', 'crawl', 'jobbole'])
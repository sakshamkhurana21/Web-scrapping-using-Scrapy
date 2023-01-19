#!/usr/bin/env python
# coding: utf-8

# In[9]:


import scrapy
from IPython import get_ipython


# In[10]:


class QuotesSpider(scrapy.Spider):
    name="quotes_spider"
    def start_request(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
            'https://quotes.toscrape.com/page/3/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        page_id=response.url.split("/")[-2]
        filename="quotes-%s.html"% page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved file %s" % filename)


# In[ ]:





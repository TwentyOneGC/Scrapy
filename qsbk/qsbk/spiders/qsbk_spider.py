# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = 'https://www.qiushibaike.com'
    def parse(self, response):
        contentLefts = response.xpath("//div[@id='content-left']/div")
        for contentLeft in contentLefts:
            author = contentLeft.xpath(".//h2/text()").get().strip()
            content = contentLeft.xpath(".//div[@class='content']//text()").getall()
            print(content)
            content = "".join(content).strip()
            # duanzi = {'author':author, 'content':content}
            item = QsbkItem(author=author, content=content)
            yield item
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain + next_url, callback=self.parse)
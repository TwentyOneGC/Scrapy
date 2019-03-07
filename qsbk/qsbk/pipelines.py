# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter   #json导出器
from scrapy.exporters import JsonLinesItemExporter
import datetime
class QsbkPipeline(object):
    def __init__(self):
        self.f = open("qsbk.json", "wb")
        self.exporter = JsonLinesItemExporter(self.f, ensure_ascii=False, encoding='utf-8')
        self.start_time = datetime.datetime.now()
    def open_spider(self, spider):
        print("[{}]开始抓取数据".format(self.start_time))

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


    def close_spider(self, spider):
        self.f.close()
        end_time = datetime.datetime.now()
        print("数据抓取完毕,总计用时：{}".format(end_time-self.start_time))










# class QsbkPipeline(object):
#     def __init__(self):
#         self.f = open("qsbk.json", "w", encoding='utf-8')
#
#     def open_spider(self, spider):
#         print("开始抓取数据")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         # print(item_json)
#         self.f.write(item_json + "\n")
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()
#         print("数据抓取完毕")
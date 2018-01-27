# -*- coding: utf-8 -*-
import json
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class SubtitlesPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        file = crawler.settings.get('file')
        return cls(file)

    def __init__(self, file):
        self.file = file if file is not None else 'subtitles.json'

    def process_item(self, item, spider):
        #with open(self.file, 'a', encoding='utf-8') as f:
        folder = os.path.dirname(self.file)
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(self.file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

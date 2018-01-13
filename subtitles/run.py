# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from http.server import HTTPServer
from webserver.requesthandler import LocalRequestHandler
import requests
import patoolib
import urllib
import json
import sys
import re

SPIDERS_NAME = ['zimuku']

def run_crawler(argv):
    movie = 'test'
    file = 'subtitles.json'
    if len(argv) > 0:
        for arg in argv:
            k = arg.split('=')[0]
            v = arg.split('=')[1]
            if k == 'movie':
                movie = v
            if k == 'file':
                file = v

    settings = get_project_settings()
    settings.set('file', file)
    runner = CrawlerRunner(settings)
    for name in SPIDERS_NAME:
        runner.crawl(name, movie)
    runner.join().addBoth(lambda _: reactor.stop())

    # the script will block here until all crawling jobs are finished
    reactor.run()

def run_web_server(port=8080):
    server_address = ('', port)
    server = HTTPServer(server_address, LocalRequestHandler)
    print('Starting web server at %d port' % port)
    server.serve_forever()

def download_package(url, path):
    response = requests.get(url)
    urllib.parse.unquote('[zmk.tw]Test%20Your%20Brain%202011%20720p%20Bluray%20DTS%205.1%20x264-DON.rar')
    if response.status_code != 200:
        print("Download subtitle failed! [%s]" % url)
        return
    file_quote = re.findall('(?<=filename=")\S+(?=")', response.headers.get('Content-Disposition'))
    file_path = path + urllib.parse.unquote(file_quote[0])
    with open(file_path, 'wb') as f:
        f.write(response.content)
    return file_path

if __name__ == '__main__':
    # run_web_server()
    # print(sys.argv[1:])
    argv = ['movie=test', 'file=subtitles.json']
    run_crawler(argv)
    subtitle_list = []
    with open('subtitles.json', 'r', encoding='utf-8') as f:
        for line in f:
            subtitle_list.append(json.loads(line))
    file_path = download_package(subtitle_list[0]['download_url'][0], './')
    patoolib.extract_archive(file_path, outdir='./')



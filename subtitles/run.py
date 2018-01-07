# -*- coding: utf-8 -*-
import sys
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from http.server import HTTPServer
from webserver.requesthandler import LocalRequestHandler

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


if __name__ == '__main__':
    run_web_server()
    # print(sys.argv[1:])
    # argv = ['movie=test', 'file=subtitles.json']
    # run_crawler(argv)


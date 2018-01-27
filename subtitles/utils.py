# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from multiprocessing import Process
from http.server import HTTPServer
from webserver.requesthandler import LocalRequestHandler
import requests
import patoolib
import urllib
import json
import re

def _exec_crawler(movie, file):
    SPIDERS_NAME = ['zimuku']
    settings = get_project_settings()
    settings.set('file', file)
    runner = CrawlerRunner(settings)
    for name in SPIDERS_NAME:
        runner.crawl(name, movie)
    runner.join().addBoth(lambda _: reactor.stop())
    # the script will block here until all crawling jobs are finished
    reactor.run()

def run_crawler(movie, file):
    p = Process(target=_exec_crawler, args=(movie, file, ))
    p.start()
    p.join()

def run_web_server(port=8080):
    server_address = ('', port)
    server = HTTPServer(server_address, LocalRequestHandler)
    print('Starting web server at %d port' % port)
    server.serve_forever()

def get_subtitle(src_file, dst_path):
    if src_file.endswith(('zip', 'rar')):
        patoolib.extract_archive(src_file, outdir=dst_path)

def parse_args(argv):
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
    return movie, file

def download_package(url, path):
    response = requests.get(url)
    if response.status_code != 200:
        print("Download subtitle failed! [%s]" % url)
        return
    file_quote = re.findall('(?<=filename=")\S+(?=")', response.headers.get('Content-Disposition'))
    file_path = path + urllib.parse.unquote(file_quote[0])
    with open(file_path, 'wb') as f:
        f.write(response.content)
    return file_path

def parse_movie(movie_quote):
    # Better Watch Out 2016 BluRay 1080p AAC x264-MTeamPAD ==> | Need format.
    # Better.Watch.Out.2016.BluRay.1080p.AAC.x264-MTeamPAD <== |
    movie_quote = movie_quote.replace(' ', '.')
    # Crayon.Shinchan.My.Moving.Story.Cactus.Large.Attack.2015.BluRay.iPad.1080p.AAC.x264-MTeamPAD
    # [name][year][type][video_resolution][audio_codec][video_codec][team]
    m = re.search(r'(?:[\u4e00-\u9fa5a-zA-Z0-9\-]+\.)+?\d{4}', movie_quote)
    return m[0]


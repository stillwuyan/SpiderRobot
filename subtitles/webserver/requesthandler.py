# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse   #, parse_qs
import os
import json

class LocalRequestHandler(BaseHTTPRequestHandler):
    movies_path = "J:/Download"
    ext_list = ('.srt', '.ass', '.mta', '.db')
    def _set_headers(self, content_type='application/json'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_file(self, filename):
        if filename[-4:] == '.css':
            self._set_headers('text/css')
        elif filename[-5:] == '.json':
            self._set_headers('application/json')
        elif filename[-3:] == '.js':
            self._set_headers('application/javascript')
        elif filename[-4:] == '.ico':
            self._set_headers('image/x-icon')
        else:
            self._set_headers('text/html')
        with open(filename, 'rb') as f:
            self.wfile.write(f.read())

    def do_GET(self):
        path = urlparse(self.path).path
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public')
        if path == '/':
            filename = root + '/index.html'
            self._send_file(filename)
        elif path == '/movies':
            self._set_headers()
            movie_list = os.listdir(self.movies_path)
            movie_list = list(filter(lambda x: not x.endswith(self.ext_list), movie_list))
            self.wfile.write(json.dumps(movie_list).encode(encoding='utf-8'))
        elif path == '/query':
            query = urlparse(self.path).query
            query_dict = dict(q.split('=') for q in query.split('&'))   # { 'key' : 'value' }
            # Or use parse_qs
            # query_dict = parse_qs(query)                              # { 'key' : ['value'] }
            print(urlparse(self.path))
        else:
            filename = root + self.path
            self._send_file(filename)

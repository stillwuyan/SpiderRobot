# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote#, parse_qs
import os
import json

class LocalRequestHandler(BaseHTTPRequestHandler):
    root_path = "J:/Download/"
    current_path = root_path
    ext_list = ('.mta', '.db')
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

    def _send_filelist(self, path):
        self._set_headers()
        file_list = os.listdir(path)
        file_list = list(filter(lambda x: not x.endswith(self.ext_list), file_list))
        response = {
            'type': 'folder',
            'data': file_list
        }
        self.wfile.write(json.dumps(response).encode(encoding='utf-8'))

    def do_GET(self):
        path = urlparse(self.path).path
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public')
        if path == '/':
            filename = root + '/index.html'
            self._send_file(filename)
        elif path == '/movies':
            self._send_filelist(self.root_path)
        elif path == '/query':
            query = urlparse(self.path).query
            query_dict = dict(q.split('=') for q in query.split('&'))   # { 'key' : 'value' }
            # Or use parse_qs
            # query_dict = parse_qs(query)                              # { 'key' : ['value'] }
            file = self.current_path + unquote(query_dict['movie'], encoding='utf-8')
            if os.path.isdir(file):
                self.current_path = file + '/'
                self._send_filelist(file)
            elif os.path.isfile(file):
                self._set_headers()
                response = {
                    'type': 'message',
                    'data': 'this is a file: %s' % file
                }
                self.wfile.write(json.dumps(response).encode(encoding='utf-8'))
            else:
                self._set_headers()
                response = {
                    'type': 'message',
                    'data': 'unknown file type: %s' % file
                }
                self.wfile.write(json.dumps(response).encode(encoding='utf-8'))
        else:
            filename = root + self.path
            self._send_file(filename)

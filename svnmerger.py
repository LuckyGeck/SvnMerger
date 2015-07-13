#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import send_from_directory
from flask import render_template
import os


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'walrus.png',
                               mimetype='image/png')

@app.route('/')
@app.route('/index.html')
def hello(name=None):
    return render_template('index.html')

def main(args):
    app.run(host=args.host, port=args.port)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('Svn Merger - tool for merging commits from trunk to stable',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--host', default='0.0.0.0',
                        help='hostname for web ui to listen on')
    parser.add_argument('-p', '--port', type=int,
                        help='port for web ui to listen on')
    parser.add_argument('-c', '--config', type=argparse.FileType('r'),
                        help='path to config file')
    main(parser.parse_args())

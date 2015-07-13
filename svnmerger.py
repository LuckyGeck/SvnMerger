#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


def main(args):
    app = Flask(__name__)
    app.run(host=args.host, port=args.port)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('Svn Merger - tool for merging commits from trunk to stable',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-h', '--host', default='http://0.0.0.0',
                        help='hostname for web ui to listen on')
    parser.add_argument('-p', '--port', type=int, default=-1,
                        help='port for web ui to listen on')
    parser.add_argument('-c', '--config', type=argparse.FileType('r'),
                        help='path to config file')
    main(parser.parse_args())

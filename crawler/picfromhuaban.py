#!usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import re
import sys
import os
from threading import Thread
import time
import random
import hashlib


class huaban(object):

    url = None
    dirPath = None
    __md5 = None
    fname = None

    def __init__(self):
        self.host = "http://huaban.com"
        self.url = "http://tieba.baidu.com/qqbwww/"
        self.dirPath = "F://huaban/"
        if os.path.isdir(self.dirPath):
            pass
        else:
            os.mkdir(self.dirPath)

    def getBoards(self, username):
        url = self.host + "/" + username
        res = urllib2.urlopen(url)
        html = res.read()
        rc = '"file_id":(\d*)'
        boards = re.findall(rc, html, re.MULTILINE | re.DOTALL)
        return boards

    def getPins(self, board):
        url = self.host + "/" + board
        res = urllib2.urlopen(url)
        html = res.read()
        rc = '<img src="(http://img.hb.aicdn.com/[^"]*)"[^>]*>'
        pins = re.findall(rc, html, re.MULTILINE | re.DOTALL)
        return pins

    def saveImg(self, images):
        j = 0
        for i in images:
            j += 1
            fname = self.dirPath + time() + "_" + str(j) + ".jpg"

            res = urllib2.urlopen(i)
            pic = res.read()

            f = open(fname, 'wb')
            f.write(pic)
            f.close()


if __name__ == '__main__':
    h = huaban()
    boards = h.getBoards('qqbwww')
    print boards
    for board in boards:
        pins = h.getPins(board)
        print pins
        h.saveImg(pins)

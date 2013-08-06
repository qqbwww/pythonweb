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


class tieba(object):

    url = None
    dirPath = None
    __md5 = None
    fname = None

    def __init__(self):
        self.host = "http://tieba.baidu.com"
        self.url = "http://tieba.baidu.com/f?kw=%BA%A3%D4%F4%CD%F5&tp=0&pn="
        self.dirPath = "F://tieba/"
        self.__md5 = hashlib.md5()
        if os.path.isdir(self.dirPath):
            pass
        else:
            os.mkdir(self.dirPath)

    def getImagesFromUrl(self, url):
        self.fname = url.split('/')[2]
        url = self.host + url
        res = urllib2.urlopen(url)
        html = res.read()
        #rc = '<img class="BDE_Image" src="([^"]*)"[^>]*>'
        #勉强可以
        #rc = '"(http://imgsrc.baidu.com/forum/[^?"]*)[?]?[^"]*"'
        rc = '<img pic_type="\d" class="BDE_Image" src="([^"]*)"[^>]*>'
        html = re.findall(rc, html, re.MULTILINE | re.DOTALL)
        return html

    def getTieziUrl(self, page):
        url = self.url + str(page * 50)
        res = urllib2.urlopen(url)
        html = res.read()
        rc = '<a href="([^"]*)" title="[^"]*" target="[^"]*" class="[^"]*"[^>]*>'
        html = re.findall(rc, html, re.MULTILINE | re.DOTALL)
        return html

    def saveImg(self, images):
        j = 0
        for i in images:
            j += 1
            fname = self.dirPath + self.fname + "_" + str(j) + ".jpg"

            res = urllib2.urlopen(i)
            pic = res.read()

            f = open(fname, 'wb')
            f.write(pic)
            f.close()


class catch(Thread):
    startPage = None
    endPage = None

    def __init__(self, start, end):
        Thread.__init__(self)
        self.startPage = start
        self.endPage = end

    def run(self):
        loop = range(self.startPage, self.endPage + 1)
        for i in loop:
            t = tieba()
            urls = t.getTieziUrl(i)
            for url in urls:
                imgs = t.getImagesFromUrl(url)
                t.saveImg(imgs)
            print "get page %d success" % i
            sys.stdout.flush()

if __name__ == '__main__':
    '''
    t = tieba()
    urls = t.getImagesFromUrl('/p/2511019984')
    for url in urls:
        if (url.find('class="BDE_Image"') > 0):
            print url
    '''
    maxPage = 500
    threadSum = 1
    if threadSum > maxPage:
        threadSum = maxPage
    urlCount = maxPage / threadSum

    for i in range(0, threadSum):
        c = catch(i * urlCount, (i + 1) * urlCount - 1)
        c.start()

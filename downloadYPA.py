#!/usr/bin/env python

from pyquery import PyQuery as pq
import urllib
import os

index = "http://ypa.ee.ncku.edu.tw/"
dataindex = './data/ypa/'
for chromo in range(16,17):
    url = "http://ypa.ee.ncku.edu.tw/do?act=chr&chr=" + str(chromo)
    q = pq(url=url)
    datadir = dataindex + "chr" + str(chromo) + "/"
    for tr in q('table.far')('tbody')('tr').items():
        genename = tr('td')('a[class!=icon]').text()
        geneurl = index+tr('td')('a[class!=icon]').attr['href']
        if not os.path.exists(datadir):
            os.makedirs(datadir)
        fout = open(datadir + genename, "w")
        geneweb = pq(url=geneurl)
        #print "find a %s in %s \n" % (genename, geneurl)
        fileurl = ""
        for furl in geneweb('div.grid_12')('p.top').items():
            if 'download' in furl('a').attr['href']:
                fileurl = index + furl('a').attr['href']
                print "find a download url %s\n" % fileurl
                break
        else:
            continue

        genefile = pq(url=fileurl)
        #print genefile.text()
        fout.write(genefile.text())
        fout.close()

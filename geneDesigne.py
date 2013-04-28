#!/usr/bin/env python

from __future__ import division
from flask import Flask
from BioManager import *

app = Flask(__name__)
bio = BioManager()
randColor = ['#0099ff', '#00ff99',
            '#ff0099', '#ff9900',
            '#99ff00', '#9900ff']

@app.route('/<message>')
def output(message):
    result = bio.parse()
    totalLen = len(bio.seq)
    html = '<table border="1" cellspacing="0"> <tr>'
    result = [a for a in result]
    resultNum = len(result)
    for index in xrange(1, resultNum-1):
        html += '<td width="{1}px" bgColor={2}>{0}</td>'.format(\
                result[index]['name'], \
                (result[index]['end']-result[index]['start'])\
                /( totalLen/resultNum ) * (1/0.06188888888),\
                randColor[index%6])
    html += '</table>'
    return html

if __name__ == '__main__':
    app.run(debug=True)

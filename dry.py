#!/usr/bin/env python

from flask import Flask
from BioManager import *

app = Flask(__name__)
bio = BioManager()

@app.route('/<message>')
def output(message):
    result = bio.parse()
    html = '<table border="1"> <tr>'
    result = [a for a in result]
    for index in xrange(1, len(result)-1):
        html += "<td>{0}</td>".format(\
                result[index]['name'])
    html += '</table>'
    return html

if __name__ == '__main__':
    app.run(debug=True)

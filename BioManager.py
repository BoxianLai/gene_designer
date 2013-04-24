#!/usr/bin/env python

from Bio import SeqIO
class BioManager:
    def get_first_CDS(self, parser):
        for feat in parser.features:
            if feat.type == 'CDS':
                yield feat

    def parse(self, filename='sequence.gb', filetype='genbank'):
        record = SeqIO.parse(filename, filetype).next()
        for a in self.get_first_CDS(record):
            if ('gene' in a.qualifiers):
                yield dict(name=a.qualifiers['gene'][0], \
                            start=a.location.start, \
                            end = a.location.end)


if __name__ == '__main__':
    app = BioManager()
    result = app.parse()
    print ( [ a for a in result] )



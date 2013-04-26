#!/usr/bin/env python

from Bio import SeqIO

class BioManager:
    seq = ""
    record = ""
    mRNA = []

    def __init__(self, filename='t7.gb', filetype='genbank'):
        self.record = SeqIO.parse(filename, filetype).next()
        self.seq = self.record.seq

    def get_first_CDS(self, parser):
        for feat in parser.features:
            if feat.type == 'CDS':
                yield feat

    def parse(self, filename='t7.gb', filetype='genbank'):
        for feat in self.record.features:
            if feat.type == 'mRNA':
                mrna = [{}]
                mrna[0]['start'] = int(feat.location.start)
                mrna[0]['end']   = int(feat.location.end)
                mrna[0]['tag']   = 'mRNA'
                self.mRNA.append(mrna)
            elif feat.type == 'CDS':
                cds = {}
                cds['start'] = int(feat.location.start)
                cds['end']   = int(feat.location.end)
                cds['tag'] = 'CDS'
                cds['translation'] = feat.qualifiers['translation']
                self.mRNA[len(self.mRNA)-1].append(cds)
        return self.mRNA


if __name__ == '__main__':
    app = BioManager()
    result = app.parse()
    for rna in result:
        for seq in rna:
            if seq['tag'] == 'mRNA':
                print "{0}({1}-{2})".format(seq['tag'],\
                                seq['start'], seq['end'])
            if seq['tag'] == 'CDS':
                print "-->{0}({1}-{2})".format(seq['tag'],\
                                seq['start'], seq['end'])
        raw_input("")



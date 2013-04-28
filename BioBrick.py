#!/usr/bin/env python

from Bio import SeqIO
import re
class promoter:
    start = 0
    end = 0
    img_src = "./static/promoter.jpg"
    def __init__(start, end):
        self.start = start
        self.end = end

class BioBrick:
    """
        parse BioBrick File and so on

        TTAA: TTAA Box position[start:end:name:desc]
        TFs:  TF.... WTF
        TSS:  Transcription Start Site
        Start:Code Sequence Start
        Stop: Code Sequence Stop
        EndUTR: the end of 3' UTR
        geneseq: the seq of gene before code sequence
        flg:  1:start<stop
              2:stop>start
    """

    names = ["Promoter","5'UTR", "3'UTR", "Coding"]

    TTAA = []
    TFs = []
    TSS = 0
    Start = 0
    Stop = 0
    EndUTR = 0
    geneseq = ""
    flg = 1

    def __init__(self, filename, filetype):
        desc = ""
        for seq in SeqIO.parse(filename, filetype):
            if self.geneseq in seq.seq:
                self.geneseq = str(seq.seq)
            if not seq.name in self.names:
                TF = {}
                TF['name'] = seq.name
                TF['desc'] = seq.description
                TF['start'],TF['end'] = ( int(i) \
                        for i in re.search('Range=.:(\d+)~(\d+)',\
                                        TF['desc']).groups() )
                TF['seq']  = seq.seq[:]
                if TF['name'] != 'TTAA':
                    self.TFs.append(TF)
                else:
                    self.TTAA.append(TF)
            else:
                desc += seq.description
        self.TFs.sort(key=lambda a:a['start'])
        self.TTAA.sort(key=lambda a:a['start'])
        self.TSS = int( re.search("TSS=(\d+)", desc).group(1) )
        self.Start = int( re.search("Start codon=(\d+)", desc).group(1) )
        self.Stop = int( re.search("Stop codon=(\d+)", desc).group(1) )
        self.EndUTR = int( re.search("End of 3'UTR=(\d+)", desc).group(1) )
        if self.Start < self.Stop:
            flg = 1
        else:
            flg = 0


if __name__ == "__main__":
    filename = raw_input("filename: ")
    b = BioBrick(filename, "fasta")
    print b.TFs, b.TSS, b.Start, b.Stop, b.EndUTR
    print b.geneseq

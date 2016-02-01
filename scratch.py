__author__ = 'lanx'
# -*- coding: utf-8 -*-
import MeCab
class DocumentAnalyzer():
    name = "DA"
    def __init__(self):
        return

    def da_print(self):
        print self.name



def apply_mecab(txt):
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ko-dic')
    output = m.parse(txt)
    output = output.split('\n')
    output = [item.split(',') for item in output]
    tagged = []
    for line in output:
        if line[0]=='' or line[0]=='EOS':
            continue
        tagged.append(line[0])
    return tagged

def extract_noun_only(txt):
    tagged = apply_mecab(txt)
    tagged = map(lambda x: x.split('\t'), tagged)
    tagged = filter(lambda x: len(x)>1 and x[1][:2] == 'NN', tagged)
    tagged = map(lambda x: x[0], tagged)
    return tagged

def hangul_unicode(txt):
    return unicode(txt, "utf-8")
    # cases = []
    # cases.append( lambda t: t.encode('unicode-escape').decode('string-escape').decode('utf8') )
    # cases.append( lambda t: t.encode('unicode-escape').decode('string-escape').decode('euckr') )
    # cases.append( lambda t: t if t.encode('utf8') else '' )
    # cases.append( lambda t: t.decode('utf8') )
    # cases.append( lambda t: t.decode('euckr') )
    # for case in cases:
    #     try:
    #         result = case(txt)
    #         if not '\\' in result:
    #             return result
    #     except (UnicodeEncodeError, UnicodeDecodeError):
    #         pass
    # return txt

test_file = 'test/news1.txt'
with open(test_file,'r') as f:
    lines = f.readlines()

k = DocumentAnalyzer()
k.da_print()

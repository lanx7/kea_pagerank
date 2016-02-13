__author__ = 'lanx'
# -*- coding: utf-8 -*-

from document_analyzer import DocumentAnalyzer


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
    #txt = f.read()

k = DocumentAnalyzer()
sentences = k.sentence_extract2(lines)
keywords1 = k.keyword_extract(sentences)
keywords2 = k.keyword_extract_rank(sentences)

for (key, value) in keywords1:
    print key, value

for (key, value) in keywords2:
    print key, value





__author__ = 'lanx'
# -*- coding: utf-8 -*-
import MeCab
import operator

class DocumentAnalyzer():
    MAX_KEYWORD = 10
    name = "DA"
    def __init__(self):
        pass

    def da_print(self):
        print self.name

    # Input: Lines of Raw Text
    def sentence_extract(self, txt):
        tokens = txt.split('.')
        for idx, s in enumerate(tokens):
            print idx, s

    def sentence_extract2(self,lines):
        sentences = []
        for idx, line in enumerate(lines):
            #print idx, line
            if line.strip() == '':
                continue
            sentences.append(line.rstrip())
        return sentences

    def keyword_extract(self, sentences):
        words = []
        for sentence in sentences:
            tokens = extract_noun_only(sentence)
            words.extend(tokens)


        word_frequency = {}
        for w in words:
            word_frequency.setdefault(w, 0)
            word_frequency[w] += 1

        sorted_word = sorted(word_frequency.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_word[:self.MAX_KEYWORD]

        #print word_frequency['브라질']

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
    #tagged = filter(lambda x: len(x)>1 and x[1][:2] == 'NN', tagged)
    tagged = filter(lambda x: len(x)>1 and (x[1][:3] == 'NNP' or x[1][:3] =='NNG'), tagged)
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
    #txt = f.read()

k = DocumentAnalyzer()
sentences = k.sentence_extract2(lines)
keywords = k.keyword_extract(sentences)
for k in keywords:
    print k[0], k[1]




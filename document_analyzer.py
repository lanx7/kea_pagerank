__author__ = 'lanx'
# -*- coding: utf-8 -*-


import MeCab
import operator
from utils import *
import pagerank

class DocumentAnalyzer():
    MAX_KEYWORD = 10
    def __init__(self):
        pass

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

    def keyword_extract_rank(self, sentences):
        words = []
        word_frequency = {}
        sequence_frequency = {}
        for sentence in sentences:
            tokens = self.extract_noun_only(sentence)
            prev = 'NULL'
            for t in tokens:
                word_frequency.setdefault(t, 0)
                word_frequency[t] += 1
                if prev != 'NULL':
                    sequence_frequency.setdefault(tuple((prev,t)),0)
                    sequence_frequency[tuple((prev,t))] += 1
                prev = t
            #words.extend(tokens)

        sorted_word = sorted(word_frequency.items(), key=operator.itemgetter(1), reverse=True)
        nodes = []
        edges = []
        for w in sorted_word:
            #print w[0], w[1]
            nodes.append(tuple((w[0],w[1])))

        sorted_edge = sorted(sequence_frequency.items(), key=operator.itemgetter(1), reverse=True)
        for e in sorted_edge:
            #print e[0][0], e[0][1], e[1]
            edges.append(tuple((e[0][0],e[0][1], e[1])))

        p = pagerank.PageRank(nodes, edges)
        p.print_graph()
        #print p.get_transition_table()
        p.calc_rank()
        result = p.get_rank()
        result = sorted(result, key=operator.itemgetter(1), reverse=True)
        return result[:self.MAX_KEYWORD]


    def keyword_extract(self, sentences):
        words = []
        for sentence in sentences:
            tokens = self.extract_noun_only(sentence)
            words.extend(tokens)

        word_frequency = {}
        for w in words:
            word_frequency.setdefault(w, 0)
            word_frequency[w] += 1

        sorted_word = sorted(word_frequency.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_word[:self.MAX_KEYWORD]

        #print word_frequency['브라질']

    def apply_mecab(self, txt):
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

    def extract_noun_only(self, txt):
        tagged = self.apply_mecab(txt)
        tagged = map(lambda x: x.split('\t'), tagged)
        #tagged = filter(lambda x: len(x)>1 and x[1][:2] == 'NN', tagged)
        tagged = filter(lambda x: len(x)>1 and (x[1][:3] == 'NNP' or x[1][:3] =='NNG'), tagged)
        tagged = map(lambda x: x[0], tagged)
        return tagged

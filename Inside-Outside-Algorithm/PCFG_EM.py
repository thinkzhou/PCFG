__author__ = 'zhouyang'
import random
from collections import defaultdict
from Expected_count import EX_COUNT
class PCFG_EM:
    def __init__(self, train_file, CFG):
        self.sentences = self.read_train_data(train_file)
        self.train_num = len(self.sentences)
        self.cfg = CFG
        self.q = self.init_q()

    def read_train_data(self,file_name):
        sentences = []
        with open(file_name) as f:
            for line in f.readlines():
                if len(line):
                    sentences.append(line.strip())
        return sentences
    def init_q(self):
        q = defaultdict(float)
        for A in self.cfg.noterminals:
            c = 0
            for (A2,w) in self.cfg.unary_rules:
                if(A2==A):
                    c = c + 1
            for (A2,B,C) in self.cfg.binary_rules:
                if(A2==A):
                    c = c + 1
            sum = 0.0
            for (A2,w) in self.cfg.unary_rules:
                if(A2==A):
                    if c == 1:
                        q[tuple([A,w])] = 1.0- sum
                    else:
                        q[tuple([A,w])] = random.uniform(0,1.0-sum)
                    c = c - 1
                    sum = sum + q[tuple([A,w])]
            for (A2,B,C) in self.cfg.binary_rules:
                if(A2==A):
                    if c == 1:
                        q[tuple([A,B,C])] = 1.0- sum
                    else:
                        q[tuple([A,B,C])] = random.uniform(0,1.0-sum)
                    c = c - 1
                    sum = sum + q[tuple([A,B,C])]
        return q

    def EM(self, iter_num=50):
        q = self.q
        for it in range(1,iter_num):
            print('start the',it,'th iterator')
            f = defaultdict(float)
            for (A,w) in self.cfg.unary_rules:
                f[tuple([A,w])] = 0.0
            for (A,B,C) in self.cfg.binary_rules:
                f[tuple([A,B,C])] = 0.0
            for i in range(1,self.train_num+1):
                sentence = self.sentences[i-1]
                ex_count = EX_COUNT(sentence=sentence,CFG=self.cfg,q =q)
                count = ex_count.get_count()
                for (A,w) in self.cfg.unary_rules:
                    f[tuple([A,w])] += count.get(tuple([A,w]))
                for (A,B,C) in self.cfg.binary_rules:
                    f[tuple([A,B,C])] += count.get(tuple([A,B,C]))


            for A in self.cfg.noterminals:
                sum_f = 0.0
                for (A2,w) in self.cfg.unary_rules:
                    if (A2==A):
                        sum_f += f[tuple([A,w])]
                for (A2,B,C) in self.cfg.binary_rules:
                    if (A2 == A):
                        sum_f += f[tuple([A,B,C])]

                for (A2,w) in self.cfg.unary_rules:
                    if(A2 == A and sum_f):
                        q[tuple([A,w])] = (f[tuple([A,w])] / sum_f)
                    if (A2 == A  and f[tuple([A,w])] == 0.0):
                        q[tuple([A,w])]=0.0

                for (A2,B,C) in self.cfg.binary_rules:
                    if(A2 == A and sum_f):
                        q[tuple([A,B,C])] = (f[tuple([A,B,C])] / sum_f)
                    if(A2 ==A and f[tuple([A,B,C])] == 0.0):
                        q[tuple([A,B,C])]=0.0
            print('OK')
        return q

    def gen_sentence(self, symbol):
        '''
        Generalize sentence from pcfg
        :param symbol:
        :return:
        '''
        tokens=[]
        for (A,w) in self.cfg.unary_rules:
            if(A == symbol):
                num = int(self.q.get((A,w))*1000)
                for i in range(num):
                    tokens.append(w)
        for (A,B,C) in self.cfg.binary_rules:
            if (A==symbol):
                num = int(self.q.get((A,B,C)) * 1000)
                for i in range(num):
                    tokens.append(tuple([B,C]))
        inx = int(random.uniform(0,len(tokens)))
        next_symbol = tokens[inx]
        if isinstance(next_symbol,tuple):
            return self.gen_sentence(next_symbol[0])+' '+self.gen_sentence(next_symbol[1])
        else:
            return next_symbol

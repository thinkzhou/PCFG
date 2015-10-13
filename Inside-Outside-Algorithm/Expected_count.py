__author__ = 'zhouyang'
from inside_outside_algorithm import Inside_Outside_ALGO
from collections import defaultdict
from inside_outside_algorithm import ishan
class EX_COUNT:
    def __init__(self, sentence, CFG, q):
        self.sentence = sentence if ishan(sentence) else sentence.split(' ')
        self.n = len(self.sentence)
        self.cfg = CFG
        self.q = q
        self.f = self.init_f()
        self.inside_outside_instance = Inside_Outside_ALGO(sentence,self.cfg,self.f)
        self.count = self.get_count()

    def get_unary_prob(self, A, w):
        return self.q.get(tuple([A,w]),0.0)

    def get_binary_prob(self, A,B,C):
        return self.q.get(tuple([A,B,C]),0.0)

    def init_f(self):
        f = defaultdict(float)
        for i in range(1,self.n+1):
            for k in  range(1,self.n+1):
                 for j in range(1,self.n+1):
                     for (A,B,C) in self.cfg.binary_rules:
                         f[tuple([A,B,C,i,k,j])] = self.get_binary_prob(A,B,C)
        for i in range(1,self.n+1):
            w = self.sentence[i-1]
            for A in self.cfg.noterminals:
                if (A,w) in self.cfg.unary_rules:
                    f[tuple([A,i])] = self.get_unary_prob(A,w)
                else:
                    f[tuple([A,i])] = 0.0
                    self.q[tuple([A,i])] = 0.0
        return f

    def get_count(self):
        count = defaultdict(float)
        for (A,B,C) in self.cfg.binary_rules:
            for i in range(1,self.n+1):
                for k in range(i,self.n+1):
                    for j in range(k+1,self.n+1):
                        count[tuple([A,B,C])] += self.inside_outside_instance.get_u_binary(A,B,C,i,k,j)
            count[tuple([A,B,C])] /= self.inside_outside_instance.Z
        for (A,w) in self.cfg.unary_rules:
            for i in range(1,self.n+1):
                if w == self.sentence[i-1]:
                    count[tuple([A,w])] += self.inside_outside_instance.get_u_unary(A,i)
            count[tuple([A,w])] /= self.inside_outside_instance.Z
        return count

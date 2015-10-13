__author__ = 'zhouyang'

from collections import defaultdict

def ishan(text):
    return all('\u4e00' <= char <= '\u9fff' for char in text)

class Inside_Outside_ALGO:
    '''
    Inside outside algorithm,given a cfg, a sentence and a protential function
    output the inside and outside probability
    '''
    def __init__(self, sentence, CFG, f):
        '''
        :param sentence: a sentence
        :param CFG:
        :param prob: a protential function that maps rules to value
        :return:
        '''
        self.sentence = sentence if ishan(sentence) else sentence.split(' ')
        self.cfg = CFG
        self.f = f
        self.n = len(self.sentence)
        self.inside = self.get_inside_terms()
        self.outside = self.get_outside_terms()
        self.Z = self.inside['S',1,self.n]



    def get_unary_rule_prob(self, X, i):
        '''
        Return the probability of rule (A->wi) where wi is the ith word in sentence
        :param X:
        :param w:
        :return:
        '''
        return self.f.get(tuple([X,i]),0.0)

    def get_binary_rule_prob(self, X, Y, Z, i, k, j):
        '''
        Return the probability of rule (X->Y Z)
        where X span substring between i and j
        Y span substring between i and k
        Z span substring between k+1 and j
        :param X:
        :param Y:
        :param Z:
        :param i:
        :param k:
        :param j:
        :return:
        '''
        return self.f.get(tuple([X,Y,Z,i,k,j]), 0.0)

    def get_inside_terms(self):
        inside = defaultdict(float)
        for i in range(1,1+self.n):
            w = self.sentence[i-1]
            for X in self.cfg.noterminals:
                if tuple([X,w]) in self.cfg.unary_rules:
                    inside[X,i,i] = self.get_unary_rule_prob(X,i)
                else:
                    inside[X,i,i] = 0.0

        for l in range(1,self.n):
            for i in range(1,self.n-l+1):
                j = i+l
                for(A,B,C) in self.cfg.binary_rules:
                    for k in range(i,j):
                        if inside[B,i,k] and inside[C,k+1,j]:
                            inside[A,i,j]+=self.get_binary_rule_prob(A,B,C,i,k,j)*inside[B,i,k]*inside[C,k+1,j]

        if inside['S',1,self.n]:
            return inside
        else:
            print(self.sentence)


    def get_outside_terms(self):
        outside = defaultdict(float)
        n = self.n
        outside['S', 1, n] = 1
        for i in range(1,n+1):
            for j in range(n,0,-1):
                if(i==1 and j ==n):
                    continue
                for (B,C,A) in self.cfg.binary_rules:
                    for k in range(1,i):
                        outside[A,i,j]+=self.get_binary_rule_prob(B,C,A,k,i-1,j)*self.inside[C,k,i-1]*outside[B,k,j]
                for (B,A,C) in self.cfg.binary_rules:
                    for k in range(j+1,n+1):
                        outside[A,i,j]+=self.get_binary_rule_prob(B,A,C,i,j,k)*self.inside[C,j+1,k]*outside[B,i,k]
        return outside

    def get_u_unary(self,A,i,j=-1):
        j = i if j==-1 else j
        return self.inside[A,i,j] * self.outside[A,i,j]

    def get_u_binary(self,A, B, C, i, k, j):
        return self.outside[A,i,j] * self.get_binary_rule_prob(A,B,C,i,k,j) * self.inside[B,i,k] * self.inside[C,k+1,j]

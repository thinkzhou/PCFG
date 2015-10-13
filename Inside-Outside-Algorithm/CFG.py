__author__ = 'zhouyang'
class CFG:
    def __init__(self, cfg_file):
        self.cfg = self.read_cfg(cfg_file)
        self.noterminals = self.get_noterminals()
        self.unary_rules = self.get_unary_rules()
        self.binary_rules = self.get_binary_rules()

    def read_cfg(self,file_name):
        '''
        Read rules from file
        :param file_name:
        :return: all rules
        '''
        CFG = []
        with open(file_name) as f:
            for line in f:
                line = line.strip().split('#')
                CFG.append((line[0],line[1]))
        return CFG

    def get_noterminals(self):
        '''
        Get noterminals in the cfg
        :return:
        '''
        noterminal = set()
        for rule in self.cfg:
            noterminal.add(rule[0])
        return tuple(noterminal)

    def get_unary_rules(self):
        '''
        Get the rules in form A->w
        where A is nonterminal and w is terminal
        :return: all rules in form A->w
        '''
        rules = []
        for rule in self.cfg:
            tmp = rule[1].split()
            if len(tmp)==1:
                rules.append(tuple([rule[0],rule[1]]))
        return rules
    def get_binary_rules(self):
        '''
        Get the rules in form A->B C
        where A,B,C are all nonterminal
        :return: all rules in form A->B C
        '''
        rules = []
        for rule in self.cfg:
            tmp = rule[1].split()
            if len(tmp) == 2:
                rules.append(tuple([rule[0], tmp[0], tmp[1]]))
        return rules

import pygame, random
class Expression:
    def __init__(self, expressionList = None):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
        }
        self.expressionList = expressionList
        self.answer = None
        self.expression = None
        self.usedOperations = self.operations.keys()
        if self.expressionList != None:
            self.answer = self.operate(self.expressionList.copy())
            self.expression = self.stringify(self.expressionList)
    def randomize_expression(self, terms, randRange):
        self.terms = terms
        self.randRange = randRange
        self.termsList = self.generate_terms(self.terms, self.randRange)
        self.operationsList = self.generate_operations(self.terms - 1)
        self.expressionList = self.integrate_operations(self.operationsList, self.termsList)
        self.expression =  self.stringify(self.expressionList.copy())
        self.answer = self.operate(self.expressionList)
    def integrate_operations(self, ops, termsList):
            lst = []
            index = -1
            for i in range(1, len(ops) + len(termsList) + 1):
                if i % 2 != 0:
                    index += 1
                    lst.append(termsList[index])
                else: lst.append(ops[index])
            return lst
    def generate_operations(self, num):
        lst = []
        for i in range(num):
            lst.append(random.choice(list(self.usedOperations))) 
        return lst

    def generate_terms(self, num, rnge):
        lst = []
        for i in range(num):
            lst.append(random.randint(rnge[0], rnge[1]))  
        return lst

    def operate(self, lst):
        for index, i in enumerate(lst):
            if i in self.usedOperations:
                prevItem = lst[index-1]
                nextItem = lst[index+1]
                lst[index] = self.operations[i](prevItem, nextItem)
                lst.remove(prevItem)
                lst.remove(nextItem)
                self.operate(lst)  
        ans = self.stringify(lst)
        return int(ans)
    def check_answer(self, num):
        if self.answer == num:
            return True
    
    def set_operations(self, lst):
        self.usedOperations = lst
    def listify(self, string):
        string = list(string)
        for index, i in enumerate(string):
            if i not in self.usedOperations:
                string[index] = int(i)
        return string
    def raw_string(self, lst):
        string = ''
        for i in lst:
            string += str(i)
        return string
    def stringify(self, lst):
        string = ''
        for index, i in enumerate(lst):
            if type(i) == type(1):
                lst[index] = str(i)
                if i < 0:
                    if lst[index-1] in self.usedOperations:
                        lst[index] = ('({})'.format(i))

        string = string.join(lst)
        return string

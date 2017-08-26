# coding=utf-8
import random
import time
# python has no absract class, we use abc to create
from abc import ABCMeta, abstractmethod
'''
I make the program to help children study arithmetic operations

Author: hatcher fang
'''


class Operation(object):
    '''abstract class'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_result(self, a, b): pass


class addOperation(Operation):
    '''concrete class'''
    def get_result(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a+b
        else:
            return 'param error'


class subOperation(Operation):
    '''concrete class'''
    def get_result(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a-b
        else:
            return 'param error'


class mulOperation(Operation):
    '''concrete class'''
    def get_result(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a*float(b)
        else:
            return 'param error'


class divOperation(Operation):
    '''concrete class'''
    def get_result(self, a, b):
        if b != 0 and isinstance(a, (int, float)) and isinstance(b, (int, float)
                                                                 ):
            return round(a/float(b), 2)
        else:
            return 'param error'


class factoryOperations(object):
    def create_factory(self, op):
        op_dict = {
            '+': addOperation(),
            '-': subOperation(),
            '*': mulOperation(),
            '/': divOperation()
        }
        opObj = op_dict.get(op)
        if not opObj:
            print '操作符格式有误！'
            return
        else:
            return opObj


class factoryOperationsWrapper(object):
    def __init__(self):
        self.rightCount = 0
        self.wrongCount = 0
        self.total = 0
        self.beginTime = time.time()

    def arithmetic_result(self):
        accuracy = self.rightCount*100/float(self.total) if self.total else 0
        print '总共 {} 道题, 您共答对 {} 道题, 答错 {} 道题 \n正确率：{}% \n总共用时：{}秒 \n{} '\
        .format(self.total, self.rightCount, self.wrongCount, accuracy,
                time.time()-self.beginTime, '太棒了！' if accuracy >= 80
                else '不错哦！' if accuracy >= 60 else
                '多多练习，你一定可以的！\n')

    def is_float(self, s):
        try:
            float(s)
            return True
        except:
            return False

    def str2Num(self, c):
        try:
            if c.isdigit():
                c = int(c)
            else:
                c = float(c)
        except:
            c = 'error type'
        return c

    def get_ab(self, floatBool, subBool, divBool, scope, op):
        while True:
            if floatBool:
                if random.randint(0, 1):
                    a = random.randint(0, scope)
                    b = random.randint(0, scope)
                else:
                    a = round(random.uniform(0, scope), 2)
                    b = round(random.uniform(0, scope), 2)
            else:
                a = random.randint(0, scope)
                b = random.randint(0, scope)
            if not subBool and a < b:
                continue
            if op == '/' and not divBool:
                d = random.randint(0, scope)
                b = random.randint(0, scope)
                a = b*d
            if op == '/' and b == 0:
                continue
            break
        return a, b

    def create_operation(self, op):
        objFactory = factoryOperations()
        opObj = objFactory.create_factory(op)
        if not opObj:
            print "factory create failed!"
            return
        op_map = {
            '+': ['加法', ' + '],
            '-': ['减法', ' - '],
            '*': ['乘法', ' x '],
            '/': ['除法', ' ÷ ']
        }
        print '请先设定{0}运算范围哦！ \n例如10以内{0}请输入：10'.format(
            op_map[op][0])
        scope = raw_input()
        while not scope.isdigit():
            print "请输入数字作为运算范围哦！"
            scope = raw_input()
        scope = int(scope)
        print '\n欢迎进入 {0} 以内{1}！'.format(scope, op_map[op][0])
        print '****************************************************'
        print '退出该运算请输入: tc'
        print '查看当前成绩请输入: ck'
        print '切换浮点运算请输入: qhfd'
        print '切换减法运算值为负数的运算请输入: qhjf'
        print '切换除法运算值为浮点数(保留两位小数)的运算请输入: qhcf'
        print '****************************************************'
        floatBool = False
        subBool = False
        divBool = False
        while 1:
            a, b = self.get_ab(floatBool, subBool, divBool, scope, op)
            print str(a) + op_map[op][1] + str(b) + ' = ?'
            c = raw_input()
            while not c.isdigit() and not self.is_float(c):
                if c == 'tc':
                    print '\n目前为止您的得分是：',
                    self.arithmetic_result()
                    print '下次再见哦！\n'
                    return
                if c == 'ck':
                    print '\n目前为止,',
                    self.arithmetic_result()
                    print '继续加油哦！\n'
                if c == 'gh':
                    print '请输入新的运算范围：'
                    scope = raw_input()
                    while not scope.isdigit():
                        print "请输入数字更换运算范围"
                        scope = raw_input()
                    scope = int(scope)
                if c == 'qhfd':
                    floatBool = not floatBool
                if c == 'qhjf':
                    subBool = not subBool
                if c == 'qhcf':
                    divBool = not divBool
                print '****************************************************'
                print '继续答题请输入数字'
                print '退出请输入：tc'
                print '查看成绩请输入：ck'
                print '更换运算范围请输入：gh'
                print '切换浮点运算请输入: qhfd'
                print '切换减法运算值为负数的运算请输入: qhjf'
                print '切换除法运算值为浮点数(保留两位小数)的运算请输入: qhcf'
                print '****************************************************'
                print str(a) + op_map[op][1] + str(b) + ' = ?'
                c = raw_input()
            c = self.str2Num(c)
            while not abs(opObj.get_result(a, b)-c) < 1e-09:
                print '很可惜，您答错了，请重新输入:'
                print str(a) + op_map[op][1] + str(b) + ' = ?'
                c = raw_input()
                while c == 'ts':
                    print opObj.get_result(a, b)
                    c = raw_input()
                while not c.isdigit() and not self.is_float(c):
                    print '请输入数字类型或输入tc跳过本题'
                    c = raw_input()
                    if c == 'tc':
                        break
                    while c == 'ts':
                        print opObj.get_result(a, b)
                        c = raw_input()
                if c == 'tc':
                    break
                c = self.str2Num(c)
                self.wrongCount = self.wrongCount + 1
                self.total = self.total + 1
                if self.wrongCount > self.rightCount and self.total % 10 == 0:
                    print '\n目前为止，',
                    self.arithmetic_result()
            if c == 'tc':
                continue
            self.rightCount = self.rightCount + 1
            self.total = self.total + 1
            print '答对了，您真聪明！\n'
            if self.total % 100 == 0:
                print '您已经答了 %d 道题, 休息一下吧！\n劳逸结合对学习事半功倍哦！\n'.format(
                    self.total)
                continue
            if self.total % 10 == 0:
                print '\n目前为止，',
                self.arithmetic_result()
                print '继续加油！\n'

    def switch_func(self):
        while 1:
            print '***********************'
            print '请输入您想做的算数练习:'
            print '加法请按：1'
            print '减法请按：2'
            print '乘法请按：3'
            print '除法请按：4'
            print '退出算术运算请输入: tc'
            print '查看成绩请输入：ck'
            print '***********************'
            print '请选择：',
            num = raw_input()
            if num == 'tc':
                print '欢迎再来哦！拜拜！'
                return
            if num == 'ck':
                print '\n目前为止,',
                self.arithmetic_result()
                print '继续加油哦！\n'
            switch_dict = {
                '1': (self.create_operation, '+'),
                '2': (self.create_operation, '-'),
                '3': (self.create_operation, '*'),
                '4': (self.create_operation, '/')
            }
            func = switch_dict.get(num)
            if not func:
                continue
            else:
                func[0](func[1])

if __name__ == '__main__':
    ca = factoryOperationsWrapper()
    ca.switch_func()

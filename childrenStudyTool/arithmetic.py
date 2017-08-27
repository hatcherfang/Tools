# coding=utf-8
import operator
import random
import time
# readline to make backspace keyspace work
import readline
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
    def __init__(self):
        self.op_map = {
            '+': ['加法', ' + ']
        }

    def get_result(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a+b
        else:
            return 'param error'


class subOperation(Operation):
    '''concrete class'''
    def __init__(self):
        self.op_map = {
            '-': ['减法', ' - ']
        }

    def get_result(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a-b
        else:
            return 'param error'


class mulOperation(Operation):
    '''concrete class'''
    def __init__(self):
        self.op_map = {
            '*': ['乘法', ' x ']
        }

    def get_result(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a*float(b)
        else:
            return 'param error'


class divOperation(Operation):
    '''concrete class'''
    def __init__(self):
        self.op_map = {
            '/': ['除法', ' ÷ ']
        }

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
        self.rightExercise = {}
        self.wrongExercise = {}
        self.scope = 0
        self.floatBool = False
        self.subBool = False
        self.divBool = False

    def clean_score(self):
        self.rightCount = 0
        self.wrongCount = 0
        self.total = 0
        self.beginTime = time.time()
        self.rightExercise = {}
        self.wrongExercise = {}

    def arithmetic_result(self):
        print '***************************************************'
        print '目前为止,',
        accuracy = self.rightCount*100/float(self.total) if self.total else 0
        print '总共 {} 道题, 您共答对 {} 道题, 答错 {} 道题 \n正确率：{}% \n总共用时：{}秒 \n{} '\
            .format(self.total, self.rightCount, self.wrongCount, accuracy,
                    time.time()-self.beginTime, '太棒了！' if accuracy >= 80
                    else '不错哦！' if accuracy >= 60 else
                    '多多练习，你一定可以的！\n')

    def exercise_done(self, flag):
        '''flag = True 正确题目
           flag = False 错误题目'''
        if not flag:
            print "做错的题目："
            print '\n'.join(self.wrongExercise) if self.wrongExercise else \
                '没有错题！'
        else:
            print "做对的题目："
            print '\n'.join(self.rightExercise) if self.rightExercise else \
                '没有正确题目！'

    def exercise_correct(self):
        if not self.wrongExercise:
            print '没有错误题目！'
        else:
            for exercise in self.wrongExercise:
                le = exercise.split()
                a = self.str2Num(le[0])
                op = le[1]
                b = self.str2Num(le[2])
                objFactory = factoryOperations()
                opObj = objFactory.create_factory(op)
                self.do_operation(a, b, exercise, opObj)

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
            pass
        return c

    def get_ab(self, op):
        while True:
            if self.floatBool:
                a = round(random.uniform(0, self.scope), 2)
                b = round(random.uniform(0, self.scope), 2)
            else:
                a = random.randint(0, self.scope)
                b = random.randint(0, self.scope)
            if not self.subBool and a < b:
                continue
            if op == '/':
                a = a*b
                if a > self.scope or b == 0:
                    continue
            break
        return a, b

    def do_operation(self, a, b, exercise, opObj):
        print exercise
        c = raw_input()
        c = self.str2Num(c)
        while isinstance(c, str) or (not abs(opObj.get_result(a, b)-c) < 1e-09):
            if c == 'tc':
                self.arithmetic_result()
                print '下次再见哦！\n'
                return True
            if c == 'ck':
                self.arithmetic_result()
                print '继续加油哦！\n'
            if c == 'gh':
                print '请输入新的运算范围(值大于0)：'
                self.scope = raw_input()
                while not self.scope.isdigit() or int(self.scope) <= 0:
                    print "请输入数字更换运算范围(值大于0)"
                    self.scope = raw_input()
                self.scope = int(self.scope)
            if c == 'qhfd':
                self.floatBool = not self.floatBool
            if c == 'qhjf':
                self.subBool = not self.subBool
            if c == 'qhcf':
                self.divBool = not self.divBool
            if c == 'ts':
                print opObj.get_result(a, b)
            if c not in ['ck', 'gh', 'qhfd', 'qhjf', 'qhcf', 'ts']:
                print '很可惜，您答错了，请重新输入数字类型或输入tg跳过本题:'
                if exercise in self.wrongExercise:
                    self.wrongExercise[exercise] = operator.add(
                        self.wrongExercise[exercise], 1)
                else:
                    self.wrongExercise[exercise] = 1
                self.wrongCount = self.wrongCount + 1
                self.total = self.total + 1
                if c == 'tg':
                    break
            print '****************************************************'
            print '继续答题请输入数字'
            print '退出请输入：tc'
            print '查看成绩请输入：ck'
            print '更换运算范围请输入：gh'
            print '切换浮点运算(结果保留两位小数)请输入: qhfd'
            print '切换减法运算值为负数的运算请输入: qhjf'
            print '****************************************************'
            print exercise
            c = raw_input()
            c = self.str2Num(c)
            if self.wrongCount > self.rightCount and self.total % 10 == 0:
                self.arithmetic_result()
        if c != 'tg':
            self.rightCount = self.rightCount + 1
            if exercise in self.rightExercise:
                self.rightExercise[exercise] = operator.add(
                    self.rightExercise[exercise], 1)
            else:
                self.rightExercise[exercise] = 1
            self.total = self.total + 1
            print '答对了，您真聪明！\n'
        if self.total % 100 == 0:
            print '您已经答了 %d 道题, 休息一下吧！\n劳逸结合对学习事半功倍哦！\n'.format(
                self.total)
            return False
        if self.total % 10 == 0:
            self.arithmetic_result()
            print '继续加油哦！\n'

    def create_operation(self, op):
        objFactory = factoryOperations()
        opObj = objFactory.create_factory(op)
        if not opObj:
            print "factory create failed!"
            return
        print '请先设定{0}运算范围哦！ \n例如10以内{0}请输入：10'.format(
            opObj.op_map[op][0])
        self.scope = raw_input()
        while not self.scope.isdigit():
            print "请输入数字作为运算范围哦！"
            self.scope = raw_input()
        self.scope = int(self.scope)
        print '******************************************************'
        print '\n欢迎进入 {0} 以内{1}！'.format(self.scope, opObj.op_map[op][0])
        print '退出该运算请输入: tc'
        print '查看当前成绩请输入: ck'
        print '切换浮点运算(保留两位小数)请输入: qhfd'
        print '切换减法运算值为负数的运算请输入: qhjf'
        print '******************************************************'
        self.floatBool = False
        self.subBool = False
        self.divBool = False
        while 1:
            a, b = self.get_ab(op)
            exercise = str(a) + opObj.op_map[op][1] + str(b) + ' = ?'
            count = 0
            while exercise in self.rightExercise:
                a, b = self.get_ab(op)
                exercise = str(a) + opObj.op_map[op][1] + str(b) + ' = ?'
                count = count + 1
                if count >= 100:
                    break
            if self.do_operation(a, b, exercise, opObj):
                break

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
            print '查看历史错题：ckct'
            print '重新计算错题：cxjsct'
            print '查看历史正确题目：ckzqtm'
            print '清空成绩输入：qk'
            print '***********************'
            print '请选择：',
            num = raw_input()
            if num == 'tc':
                print '欢迎再来哦！拜拜！'
                return
            if num == 'ck':
                self.arithmetic_result()
                print '继续加油哦！\n'
            if num == 'qk':
                self.clean_score()
                print '清空成绩！'
            if num == 'ckct':
                self.exercise_done(False)
            if num == 'ckzqtm':
                self.exercise_done(True)
            if num == 'cxjsct':
                self.exercise_correct()
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

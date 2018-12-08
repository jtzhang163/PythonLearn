import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.index = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果要可迭代(可以使用for)，必须实现__iter__方法"""

        # 返回值必须为实现了__iter__和__next__方法的类对象
        return self

    def __next__(self):
        if self.index < len(self.names):
            name = self.names[self.index]
            self.index += 1
            return name
        else:
            raise StopIteration

classmate = Classmate()
classmate.add("wang")
classmate.add("lee")
classmate.add("zhang")

#print("是否可迭代：", isinstance(classmate, Iterable))

#classmate_iterator = iter(classmate)
#print("是否是迭代器：", isinstance(classmate_iterator, Iterator))

#classmate_next = next(classmate_iterator)
#print(classmate_next)
for name in classmate:
    print(name)
    time.sleep(1)
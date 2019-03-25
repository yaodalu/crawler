# -*- coding: utf-8 -*-
def print_everything(*args):
    for count,thing in enumerate(args):
        #enumerate()迭代器
        print '{0}. {1}'.format(count,thing)

def table_things(**kwargs):
    for name,value in kwargs.items():
        print '{0} = {1}'.format(name, value)

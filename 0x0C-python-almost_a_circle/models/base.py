#!/usr/bin/python3
'''Deine class.'''


class Base:
    '''Here start clas base.'''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Define constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


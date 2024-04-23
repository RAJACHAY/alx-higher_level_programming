#!/usr/bin/python3
''' class base will be define here '''


class Base:
    ''' class base element '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''' define construteur '''
        if id is not None:
            self.id = id
        else :
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

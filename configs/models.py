#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Carrer:  
    id = 0
    name = None

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id, 
            'name': str(self.name).encode('utf-8')
        }
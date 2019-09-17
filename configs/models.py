#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Carrer:  
    id = 0
    name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id, 
            'name': self.name
        }
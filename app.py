#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dos.carrer_do import CarrerDO
from configs.models import Carrer

carrers = CarrerDO().list()
#for c in carrers:
    #print(c.to_dict())

n = Carrer(name='holña')
n = CarrerDO().add(n)
print(n.to_dict())
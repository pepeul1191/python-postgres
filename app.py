#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dos.carrer_do import CarrerDO

carrers = CarrerDO().list()
for c in carrers:
    print(c.to_dict())
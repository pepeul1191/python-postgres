#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.database import DB
from configs.models import Carrer

class CarrerDO(DB):
    def list(self):
        carrers = []
        self.cursor.execute(u"""
            SELECT * FROM carrers;
        """)
        rs = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        rpta = []
        for r in rs:
            carrers.append(
              Carrer(
                r['id'], 
                r['name'].encode('utf-8')
              )
            )
        return carrers
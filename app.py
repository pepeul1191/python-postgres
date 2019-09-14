#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.database import DB

class CarrerDO(DB):
    def list(self):
        self.cursor.execute("""
            SELECT * FROM carrers;
        """)
        rs = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        rpta = []
        for r in rs:
            print(r['name'].encode('utf-8').strip())

CarrerDO().list()
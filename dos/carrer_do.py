#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import traceback
from configs.database import DB
from configs.models import Carrer

class CarrerDO(DB):
    def list(self):
        carrers = []
        try:
            self.cursor.execute(u'''
                SELECT * FROM carrers;
            ''')
            rs = self.cursor.fetchall()
            rpta = []
            for r in rs:
                carrers.append(
                    Carrer(
                        r['id'], 
                        r['name'].encode('utf-8')
                    )
                )
        except Exception as e:
            traceback.print_exc()
        finally:
            if self.connection.close() is not None:
                self.cursor.close()
                self.connection.close()
        return carrers

    def add(self, carrer):
        try:
            self.cursor.execute('''
                INSERT INTO carrers (id, name) VALUES (DEFAULT, %s) 
                RETURNING id;
            ''', (
              carrer.name,
            ))
            carrer.id = self.cursor.fetchone()['id']
            self.connection.commit()
        except Exception as e:
            traceback.print_exc()
            if self.connection.close() is not None:
                self.connection.rollback()
        finally:
            if self.connection.close() is not None:
                self.cursor.close()
                self.connection.close()
        return carrer

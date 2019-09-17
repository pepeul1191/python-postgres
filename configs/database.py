#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
from psycopg2.extras import RealDictCursor

class DB:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', 
            port='5432',
            dbname='local', 
            user='root', 
            password='123'
        )
        self.connection.set_client_encoding('utf-8')
        self.cursor = self.connection.cursor(
            cursor_factory=RealDictCursor
        )
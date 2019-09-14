#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
from psycopg2.extras import RealDictCursor

class DB:
    def __init__(self):
        self.connection = psycopg2.connect(
          host="localhost", dbname="local", user="root", password="123"
        )
        self.cursor = self.connection.cursor(
            cursor_factory=RealDictCursor
        )


        # postgresql://localhost/local?user=root&password=123
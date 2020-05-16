#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 04:05:24 2020

@author: Alaa
"""

import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):

    def exposed_echo(self, message):
        print(message)
    
    def exposed_add(self, x, y):
        print('Result is: {}'.format(x + y))

if __name__ == "__main__":
    server = ThreadedServer(MyService, port = 18830)
    server.start()
    
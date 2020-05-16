#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 05:22:45 2020

@author: Alaa
"""

import rpyc


if __name__ == "__main__":
    print("calling the server")
    c = rpyc.connect("localhost", 18830)
    c.root.echo("Hello Server")
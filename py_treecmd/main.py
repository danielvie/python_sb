#!/usr/bin/env python

from pathlib import PurePath
import select
import sys
import re

class Node():
    def __init__(self, name) -> None:
        self.name  = name
        self.child = []

def DummyData():
    params = [
        'M       main.py', 
        'M       Makefile', 
        'A       lib/lib1.h', 
        'A       lib/lib2.h', 
        'A       lib/sub/l3.h', 
        'A       lib/sub/l4.h', 
        'A       lib/sub/l5.h', 
        'A       lib/sub/subsub/l7.h', 
        'A       lib/sub/subsub/l8.h', 
        'A       lib/sub/subsub/l9.h', 
        'A       lib/sub/subsub/l10.h', 
        'A       src/bla.txt', 
        'A       src/ble.txt', 
    ]
    
    return params


if __name__ == "__main__":
    
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        params = sys.stdin.read().split('\n') 
    else:
        params = DummyData()

    
    patt = r'(?P<type>[A-Z])\s+' \
           r'(?P<param>[\w/\\.]+)'
    
    P = []
    for param in params:
        if match := re.match(patt, param):
            value = match.groupdict()
            P.append(f"{value['param']} [{value['type']}]")

    N = {}
    
    for pi in P:
        path = PurePath(pi)
        N_   = N
        
        for part in path.parts:
            if part not in N_:
                N_[part] = {}

            N_ = N_[part]
            
    # defining joint chars
    char_pipe   = "│"
    char_middle = "├─"
    char_end    = "└─"

    def show(N, tab = 0):
        if not hasattr(show, 'pipe'):
            show.pipe = True
            print(' ')

        numel_p = len(N)

        for i,ni in enumerate(N):
            tab_ = '  '*tab
            nchildren = len(N[ni])
            
            # adding joints and pipes
            if i < numel_p - 1:
                tab_ = f'{tab_}{char_middle}'
            else:
                tab_ = f'{tab_}{char_end}'
                
            if tab == 0 and i == numel_p - 1:
                show.pipe = False
                
            if tab > 0 and show.pipe:
                tab_ = f'{char_pipe}{tab_[1:]}'

            # writing message
            msg = f'{tab_}{ni}'
            print(msg)

            # if there is no children, continue
            if nchildren == 0:
                continue
            
            show(N[ni], tab + 1)
    
    show(N)
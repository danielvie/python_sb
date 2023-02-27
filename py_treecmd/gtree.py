#!/usr/bin/env python

from pathlib import PurePath
import sys
import re

def main(params = None):
    
    if not params:
        params = sys.stdin.read().split('\n') 
    
    patt = r'(?P<type>[A-Z])\s+' \
           r'(?P<param>[\w/\\.-]+)'
    
    P = []
    for param in params:
        match = re.match(patt, param)
        if match:
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
        # instantiating persistent var in function
        if not hasattr(show, 'pipe'):
            show.pipe = True
            print(' ')

        numel_p = len(N)

        for i,ni in enumerate(N):
            nchildren = len(N[ni])
            
            # adding joints and pipes
            tab_ = f'{char_pipe}  '*tab

            if i < numel_p - 1:
                tab_ = f'{tab_}{char_middle}'
            else:
                tab_ = f'{tab_}{char_end}'
                
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

if __name__ == "__main__":
    
    from helpers import getter

    main()
    # main(getter.DummyDataFromFile('ref.txt'))

    
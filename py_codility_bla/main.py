import unittest

def solution(S:str, A) -> str:

    res:str = S[0]
    ai = A[0]

    for _ in A:
        s   = S[ai]
        res = f'{res}{s}'
        ai  = A[ai]
        if ai == 0:
            break

    return res

if __name__ == "__main__":
    
    S = "cdeo"
    A = [3,2,0,1]
    
    solution(S,A)

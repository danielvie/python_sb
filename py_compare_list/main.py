
# todo: testar casos com numero grande de elementos

A = set([  
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G' 
    ])

B = set( 
[ 
    'A',
    'B'
 ]
 )

if __name__ == "__main__":
    # I = [a for a in A if a in B]
    
    print(B.intersection(A))
    print(A & B)
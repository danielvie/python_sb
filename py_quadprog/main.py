from quadprog import solve_qp
import numpy as np

'''
Help on built-in function solve_qp in module quadprog:

solve_qp(...)
    Solve a strictly convex quadratic program
    
    Minimize     1/2 x^T G x - a^T x
    Subject to   C.T x >= b
    
    This routine uses the the Goldfarb/Idnani dual algorithm [1].
    
    References
    ---------
    ... [1] D. Goldfarb and A. Idnani (1983). A numerically stable dual
        method for solving strictly convex quadratic programs.
        Mathematical Programming, 27, 1-33.
    
    Parameters
    ----------
    G : array, shape=(n, n)
        matrix appearing in the quadratic function to be minimized
    a : array, shape=(n,)
        vector appearing in the quadratic function to be minimized
    C : array, shape=(n, m)
        matrix defining the constraints under which we want to minimize the
        quadratic function
    b : array, shape=(m), default=None
        vector defining the constraints
    meq : int, default=0
        the first meq constraints are treated as equality constraints,
        all further as inequality constraints (defaults to 0).
    factorized : bool, default=False
        If True, then we are passing :math:`R^{−1}` (where :math:`G = R^T R`)
:
'''
if __name__ == "__main__":
    
    '''
    H = eye(2) 
    f = [-5; -5]
    b = [2*ones(2,1); 0*ones(2,1)]
    A = [eye(2); -eye(2)]
    
    x = quadprog(H,f,A,b)
    
    x = 
        2.0
        2.0
    '''

    # H = np.eye(2, 2)
    # f = np.matrix([-5,-5])
    # b = np.column_stack((2*np.ones([2,1]),0*np.ones([2,1])))
    # A = np.vstack((np.eye(2), -np.eye(2)))

    G = np.array([[1, -1], [-1, 2]], dtype=np.double)
    a = np.array([-2, -6], dtype=np.double)
    C = np.array([[1, 1], [-1, 2], [2, 1]], dtype=np.double)
    b = np.array([2, 2, 3], dtype=np.double)
    
    print(' ')
    print('H:', G)
    print(' ')
    print('f:', a)
    print(' ')
    print('b:', b)
    print(' ')
    print('A:', C)
    print(' ')
    xf, f, xu, iters, lagr, iact = solve_qp(G, a, C, b)

    G = np.eye(3, 3)
    a = np.array([0, 5, 0], dtype=np.double)
    C = np.array([[-4, 2, 0], [-3, 1, -2], [0, 0, 1]], dtype=np.double)
    b = np.array([-8, 2, 0], dtype=np.double)
    
    print('dfasdfasd')

    # print(' ')
    # print('G:', G)
    # print(' ')
    # print('a:', a)
    # print(' ')
    # print('C:', C)
    # print(' ')
    # print('b:', b)
    # print(' ')

    # xf, f, xu, iters, lagr, iact = solve_qp(G, a, C, b)
    # print(xf)
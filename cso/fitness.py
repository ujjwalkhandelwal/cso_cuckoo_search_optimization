
################################################################################
#                                                                              #
#	UJJWAL KHANDELWAL                                                      #  
#	CSO (CUCKOO SEARCH OPTIMIZATION)                                       #
#	PYTHON 3.7.10                                                          #
#                                                                              #
################################################################################

#######################   IMPORT DEPENDENCIES   ################################

import numpy as np

######################## FITNESS FUNCTION 1 ######################################

def fitness_1(X):

    '''

    X: POSITION (EITHER CURRENT, LOCAL BEST OR GLOBAL BEST) OF SIZE (n,)

    2-DIMENSIONAL VECTORS (X = (x,y))

    #################################################################################

    HIMMELBLAU'S FUNCTION

    MINIMIZE f(x) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
    
    OPTIMUM SOLUTION IS x* = 3 AND y* = 2

    REPLACE 'f' BELOW WITH THIS TO TEST EXAMPLE-1

    f = (x**2 + y - 11)**2 + (x + y**2 - 7)**2

    '''
    X = np.array(X).reshape(-1,1)
    x, y = X[0][0], X[1][0]
    f = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return f

######################## FITNESS FUNCTION 2 ######################################

def fitness_2(X):

    '''

    X: POSITION (EITHER CURRENT, LOCAL BEST OR GLOBAL BEST) OF SIZE (n,)

    2-DIMENSIONAL VECTORS (X = (x,y))

    #################################################################################

    BOOTH'S FUNCTION

    MINIMIZE f(x) = (x + 2y - 7)^2 + (2x + y - 5)^2

    OPTIMUM SOLUTION IS x* = 1 AND y* = 3

    REPLACE 'f' BELOW WITH THIS TO TEST EXAMPLE-2

    f = (x + 2*y - 7)**2 + (2*x + y - 5)**2

    '''
    X = np.array(X).reshape(-1,1)
    x, y = X[0][0], X[1][0]
    f = (x + 2*y - 7)**2 + (2*x + y - 5)**2
    return f

######################## FITNESS FUNCTION 3 ######################################

def fitness_3(X):

    '''

    X: POSITION (EITHER CURRENT, LOCAL BEST OR GLOBAL BEST) OF SIZE (n,)

    2-DIMENSIONAL VECTORS (X = (x,y))

    #################################################################################

    BEALE'S FUNCTION

    MINIMIZE f(x) = (1.5 - x - xy)^2 + (2.25 - x + xy^2)^2 + (2.625 - x + xy^3)^2

    OPTIMUM SOLUTION IS x* = 3 AND y* = 0.5

    REPLACE 'f' BELOW WITH THIS TO TEST EXAMPLE-3

    f = (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2
    
    #################################################################################

    '''
    X = np.array(X).reshape(-1,1)
    x, y = X[0][0], X[1][0]
    f = (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2
    return f

def fitness_4(X):

    '''

    X: POSITION (EITHER CURRENT, LOCAL BEST OR GLOBAL BEST) OF SIZE (n,)

    2-DIMENSIONAL VECTORS (X = (x,y))

    #################################################################################

    MAXIMIZE f(x) = 2xy + 2x - x^2 - 2y^2

    OPTIMUM SOLUTION IS x* = 2 AND y* = 1

    REPLACE 'f' BELOW WITH THIS TO TEST fitness_4

    f = 2*x*y + 2*x - x**2 - 2*(y**2)
    
    #################################################################################

    '''
    X = np.array(X).reshape(-1,1)
    x, y = X[0][0], X[1][0]
    f = 2*x*y + 2*x - x**2 - 2*(y**2)
    return f

def fitness_5(X):

    '''

    X: POSITION (EITHER CURRENT, LOCAL BEST OR GLOBAL BEST) OF SIZE (n,)

    2-DIMENSIONAL VECTORS (X = (x,y))

    #################################################################################

    BIVARIATE MICHAELWICZ FUNCTION

    MINIMIZE f(x) = -sin(x)*(sin(x^2/π)^2m) - sin(y)*(sin(2y^2/π)^2m)

    OPTIMUM SOLUTION IS x* = 2.20319, AND y* = 1.57049

    REPLACE 'f' BELOW WITH THIS TO TEST EXAMPLE-5

    f = -np.sin(x)*(np.sin(x*x/np.pi)**(2*m))-np.sin(y)*(np.sin(2*y*y/np.pi)**(2*m))

    '''
    X = np.array(X).reshape(-1,1)
    m = 10
    x, y = X[0][0], X[1][0]
    f = -np.sin(x)*(np.sin(x*x/np.pi)**(2*m))-np.sin(y)*(np.sin(2*y*y/np.pi)**(2*m))
    return f

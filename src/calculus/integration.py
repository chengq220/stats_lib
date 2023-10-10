
"""
@brief        A Rieman sum approximation of integral
@param func   The function to be integrated
@param a      Lower bound of integration
@param b      Upper bound of integration
"""
@static
def riemann_approx(func, a, b)
    N = 10000
    delta_x = (b-a)/N
    steps = a
    approx = 0
    while steps < b:
    approx = approx + ((steps) ** 7)
    steps = steps + delta_x
    return (delta_x * approx)

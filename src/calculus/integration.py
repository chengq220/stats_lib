from src.util.parser import parser
"""
@brief        A Riemann sum approximation of single variable integral
@param func   The function to be integrated
@param a      Lower bound of integration
@param b      Upper bound of integration
@param vars   The variable value of the variable
"""
def integral_apprx(func, a, b, var):
    N = 10000
    p = parser(func, var, a)
    delta_x = (b-a)/N
    steps = a
    approx = 0
    print(func)
    while steps < b:
        c_val = p.evaluate()
        approx = approx + c_val
        steps = steps + delta_x
        p.value = steps
    return (delta_x * approx)

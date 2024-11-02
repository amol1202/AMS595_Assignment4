import numpy as np
import pandas as pd
import sympy as sp
import time
import matplotlib.pyplot as plt

def taylor_approx(func, start, end, degree, c):
    x = sp.symbols('x')
    f = func(x)
    taylor_series = sum(f.diff(x, n).subs(x, c) * (x - c)**n / sp.factorial(n) for n in range(degree + 1))
    f_approx = sp.lambdify(x, taylor_series, 'numpy')
    x_vals = np.linspace(start, end, 100)
    return f_approx(x_vals), x_vals

def factorial_analysis(func, start, end, c, initial_degree, final_degree, degree_step):
    x = sp.symbols('x')
    f = func(x)
    x_vals = np.linspace(start, end, 100)
    f_exact = sp.lambdify(x, f, 'numpy')
    f_vals = f_exact(x_vals)
    results = []

    for degree in range(initial_degree, final_degree + 1, degree_step):
        start_time = time.time()
        f_approx_vals, _ = taylor_approx(func, start, end, degree, c)
        elapsed_time = time.time() - start_time
        error = np.sum(np.abs(f_vals - f_approx_vals))
        results.append([degree, error, elapsed_time])

    df = pd.DataFrame(results, columns=['Degree', 'Error', 'Time'])
    df.to_csv('taylor_values.csv', index=False)

def example_run():
    x = sp.symbols('x')
    func = x * sp.sin(x)**2 + sp.cos(x)
    start, end, degree, c = -10, 10, 99, 0

    # Compute the Taylor series approximation and original function values
    f_approx_vals, x_vals = taylor_approx(func, start, end, degree, c)
    f_exact = sp.lambdify(x, func, 'numpy')
    f_vals = f_exact(x_vals)

    # Plot the results
    plt.plot(x_vals, f_vals, label='Original Function')
    plt.plot(x_vals, f_approx_vals, label='Taylor Approximation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

example_run()

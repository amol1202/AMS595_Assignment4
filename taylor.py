import numpy as np
import pandas as pd
import sympy as sp
import time
import matplotlib.pyplot as plt

def taylor_approx(func, start, end, degree, c):
    x = sp.symbols('x')
    # Construct the Taylor series up to the given degree
    taylor_series = sum(func.diff(x, n).subs(x, c) * (x - c)**n / sp.factorial(n) for n in range(degree + 1))
    f_approx = sp.lambdify(x, taylor_series, 'numpy')
    x_vals = np.linspace(start, end, 100)
    return f_approx(x_vals), x_vals

def factorial_analysis(func, start, end, c, initial_degree, final_degree, degree_step):
    x = sp.symbols('x')
    x_vals = np.linspace(start, end, 100)
    # Convert func to a callable function for NumPy
    f_exact = sp.lambdify(x, func, 'numpy')
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
    start, end, c = -10, 10, 0

    degree = 50
    f_approx_vals, x_vals = taylor_approx(func, start, end, degree, c)
    f_exact = sp.lambdify(x, func, 'numpy')
    f_vals = f_exact(x_vals)

    plt.plot(x_vals, f_vals, label='Original Function', color='blue')
    plt.plot(x_vals, f_approx_vals, label=f'Taylor Approximation (Degree {degree})', color='red', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title(f'Taylor Series Approximation vs. Original Function (Degree {degree})')
    plt.grid(True)
    plt.savefig('results/taylor_approximation.png')
    plt.show()

example_run()

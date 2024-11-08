# Amol Arora, 116491705

import numpy as np
import pandas as pd
import sympy as sp
import time
import matplotlib.pyplot as plt

def taylor_approx(func, start, end, degree, c):
    x = sp.symbols('x')
    # I start by constructing the Taylor series up to the given degree
    taylor_series = sum(func.diff(x, n).subs(x, c) * (x - c)**n / sp.factorial(n) for n in range(degree + 1))

    # For converting into a NumPy-compatible function
    f_approx = sp.lambdify(x, taylor_series, 'numpy')

    # Generating an array of x values over the specified interval
    x_vals = np.linspace(start, end, 100)
    return f_approx(x_vals), x_vals

def factorial_analysis(func, start, end, c, initial_degree, final_degree, degree_step):
    x = sp.symbols('x')
    x_vals = np.linspace(start, end, 100)
    # Convert func to a callable function for NumPy
    f_exact = sp.lambdify(x, func, 'numpy')
    f_vals = f_exact(x_vals)

    # Initialize a list to store degree, error, and computation time results
    results = []

    for degree in range(initial_degree, final_degree + 1, degree_step):
        start_time = time.time()
        f_approx_vals, _ = taylor_approx(func, start, end, degree, c)
        
        # Calculate the elapsed time for the computation
        elapsed_time = time.time() - start_time
        
        error = np.sum(np.abs(f_vals - f_approx_vals))
        results.append([degree, error, elapsed_time])

    df = pd.DataFrame(results, columns=['Degree', 'Error', 'Time'])
    # Save the results DataFrame to a CSV file
    df.to_csv('results/taylor_values.csv', index=False)

def example_run():
    # Defining the symbolic variable and the function to approximate
    x = sp.symbols('x')
    func = x * sp.sin(x)**2 + sp.cos(x)

    # Performing factorial analysis for Taylor series degrees 50 through 100, with a step size of 10
    factorial_analysis(func, -10, 10, 0, 50, 100, 10)
    start, end, c = -10, 10, 0

    degree = 50
    f_approx_vals, x_vals = taylor_approx(func, start, end, degree, c)
    f_exact = sp.lambdify(x, func, 'numpy')
    f_vals = f_exact(x_vals)

    # Plotting the original function and its Taylor series approximation
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

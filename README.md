# AMS 595 - Assignment 4: Fractal Approximation

## Overview

This project includes three main tasks implemented in Python:
1. **Mandelbrot Set**: Generating and visualizing the Mandelbrot fractal.
2. **Markov Chain Simulation**: Simulating a Markov chain with 5 states and calculating the stationary distribution.
3. **Taylor Series Approximation**: Approximating a function using Taylor series and analyzing the error and runtime.

Each task involves mathematical concepts and programming skills, focusing on fractals, stochastic processes, and function approximations.

---

## Contents

- [Mandelbrot Set](#mandelbrot-set)
- [Markov Chain Simulation](#markov-chain-simulation)
- [Taylor Series Approximation](#taylor-series-approximation)
- [Setup](#setup)
- [Usage](#usage)
- [Results](#results)
- [Project Structure](#project-structure)

---

## Mandelbrot Set

**File**: `mandelbrot.py`

This script generates an image of the Mandelbrot set within the range [-2, 1] &times; [-1.5, 1.5]. The set is defined by the recursive relation:
~~~
z(n+1) = z(n)^2 + c,  where z(0) = 0
~~~
where a complex number \(c\) belongs to the Mandelbrot set, if the iteration remains bounded.

### Key Steps
- A grid of complex numbers \( c \) is created over the specified range.
- A threshold of 50 iterations is used to determine divergence.
- The fractal image is saved in the results folder as `mandelbrot.png`.

---

## Markov Chain Simulation

**File**: `markov_chain.py`

This script simulates a Markov chain with a 5x5 transition matrix, normalizes rows, and applies the transition rule 50 times. It calculates the stationary distribution by finding the eigenvector associated with eigenvalue 1.

### Key Steps
- Generate a random 5x5 matrix and normalize rows.
- Construct a random probability vector and apply the transition rule iteratively.
- Calculate the stationary distribution using eigenvalues and eigenvectors.

---

## Taylor Series Approximation

**File**: `taylor.py`

This script approximates the function 

`f(x) = x * sin²(x) + cos(x)`

Interval size taken as [−10,10] &times; [−10,10] and using Taylor series expansion with up to 100 terms. Results are stored in a CSV file `taylor_values.csv`.

### Key Steps
- Use SymPy to compute the Taylor series expansion up to a specified degree.
- Compare the approximation with the original function and calculate error and runtime.
- Plot the original function against its Taylor approximation.

## Requirements

- Python 3.9
- NumPy
- SymPy
- Matplotlib
- Pandas

## Results

### Mandelbrot Set
The generated Mandelbrot set image is saved as `mandelbrot.png` in results folder and **demonstrates the fractal pattern of bounded complex values**.
![mandelbrot_set_image](results/mandelbrot.png)

### Markov Chain
The stationary distribution of the Markov chain converges within a tolerance of 10<sup>-5</sup>, confirming expected behavior of Markov chains in equilibrium.

### Taylor Series Approximation
The Taylor series approximation closely matches the original function around the expansion point but diverges near the edges of the interval 
[−10,10]. The error and runtime are recorded in `taylor_values.csv`.
![taylor_approximation_image](results/taylor_approximation.png)

## Project Structure

```
project/
│
├── mandelbrot.py         # Mandelbrot Set implementation
├── markov_chain.py       # Markov Chain simulation
├── taylor.py             # Taylor Series Approximation script
├── results/              # Folder containing output files
│   ├── mandelbrot.png    # Output image of Mandelbrot fractal
│   ├── taylor.png        # Output image of Taylor series approximation
│   └── taylor_values.csv  # CSV file with Taylor series error and runtime data
└── README.md             # Project documentation
```
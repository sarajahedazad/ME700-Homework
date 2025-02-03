### Table of Contents
* [An Introduction to Bisection Method](#intro)
* [Algorithm Description](#ad)
* [Requirements](#requirements)
* [Codes](#codes)
* [References](#references)
---

### An Introduction to Bisection Method <a name="intro"></a>

The Bisection Method is a fundamental algorithm in numerical analysis for finding the roots of a continuous function. This method, also known as binary chopping or interval halving, repeatedly divides an interval in half and then selects a subinterval in which a root must lie for further processing. It is particularly valued for its robustness and straightforward implementation, making it a reliable choice when dealing with functions that are well-behaved over a given range.

This method is applicable to any continuous function where the values at the endpoints of the initial interval have opposite signs, a principle known as the Intermediate Value Theorem. The Bisection Method's simplicity makes it an excellent introductory tool for understanding the concepts of error analysis and convergence in numerical solutions.

In this repository, the Bisection Method is implemented in Python, demonstrating both the theoretical and practical applications of this technique. The included code provides a clear example of the method in action, equipped with customizable parameters for tolerance levels and iterations, making it suitable for a wide range of educational and practical purposes.

---


### Algorithm Description <a name="ad"></a>

The Bisection Method is a straightforward yet powerful algorithm for finding a root of a continuous function within a specified interval where the function changes sign. Here's how the algorithm proceeds:

1. **Initialization**: 
   - Start with two initial points, a and b, such that $f(a)$ and $f(b)$ have opposite signs. This ensures that a root exists between a and b according to the Intermediate Value Theorem.

2. **Midpoint Calculation**:
   - Calculate the midpoint c of the interval $[a, b]$. This is done by the formula $c = (a + b) / 2$.

3. **Evaluation and Subinterval Selection**:
   - Evaluate the function at the midpoint, $f(c)$. 
   - Determine the subinterval that contains the root. If $f(c)$ is close enough to zero within a pre-defined tolerance, $c$ is returned as the root. The tolerances used are typically absolute tolerance (how close to zero $f(c)$ needs to be) and relative tolerance (how small the interval $[a, b]$ should become).
   - If $f(c)$ is not close enough to zero, decide which half of the interval to retain:
     - If $f(a)$ and $f(c)$ have different signs, set $b = c$.
     - Otherwise, set $a = c$.

4. **Iteration**:
   - Repeat the process, recalculating the midpoint for the new interval $[a, b]$ until the root is located within the desired tolerances or until a maximum number of iterations is reached.

5. **Convergence Check**:
   - The algorithm typically includes a condition to exit if the number of iterations exceeds a set limit, indicating that the method may not be converging.

The bisection method is highly reliable in all cases where the function continuously changes sign over the interval but can be slow to converge compared to other methods like Newton-Raphson or secant methods. Its simplicity and the assurance of convergence (given correct initial conditions) make it a popular choice for introductory numerical analysis.


---

### Requirements

`numpy library`

---

### Codes
The file `bisection_method.py` contains a class for the bisection solver.


**class *BisectionSolver***  
*Arributes*  
**abs_tol**: absolute tolerance, default = $10^{-10}$  
**rel_tol**: relative tolerance, default = $10^{-10}$  
**max_iter**: maximum number of iteration allowed to run the bisection algorithm, default = 50  
**verbose**: whether to print out the debug information at each iteration or not, default = False

*Methods:*  
**solve**  
Parameter: function,a, b. a and b are the bounds of the range in which the function is evaluated. The order does not matter. The should accept only one input and return a single float value with the size of one.      
returns: the root of the function

**How to use the bisection method:**  
The file `bisection_method.py` should be in the same directory as your working directory. Then it can be imported with the following line:
```
import bisection_method as bm
```
The algorithm can be used as the following:
```
solver = bm.BisectionSolver()  
root = solver.solve( function, bound1, bound2 )
```
For examples of how to use the method, see `tutorial.ipynb`.

---
### References
* [Lejeune Lab Graduate Course Materials: Bisection-Method](https://github.com/Lejeune-Lab-Graduate-Course-Materials/bisection-method/tree/main)
* chatGPT: was used for completing the documentation. The ["introduction"](#intro) and ["algorithm"](#ad) sections are written by the GenAI.



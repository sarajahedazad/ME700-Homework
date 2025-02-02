### Table of Contents
* [An Introduction to Bisection Method](#intro)
* [Requirements](#requirements)
* [Codes](#codes)
* [References](#references)
---

### An Introduction to Bisection Method <a name="intro"></a>

To be written


---

### Requirements

numpy library

---

### Codes

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

```
solver = BisectionSolver()  
root = solver.solve( function, bound1, bound2 )
```


---
### References
* [Lejeune Lab Graduate Course Materials: Bisection-Method](https://github.com/Lejeune-Lab-Graduate-Course-Materials/bisection-method/tree/main)



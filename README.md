# Cuckoo Search Optimization (CSO) Via Levy Flights with Python
[![GitHub license](https://img.shields.io/github/license/ujjwalkhandelwal/cso_cuckoo_search_optimization?style=flat-square)](https://github.com/ujjwalkhandelwal/cso_cuckoo_search_optimization/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/ujjwalkhandelwal/cso_cuckoo_search_optimization?style=flat-square
)](https://github.com/ujjwalkhandelwal/cso_cuckoo_search_optimization/issues)
[![GitHub forks](https://img.shields.io/github/forks/ujjwalkhandelwal/cso_cuckoo_search_optimization?style=flat-square
)](https://github.com/ujjwalkhandelwal/cso_cuckoo_search_optimization/network/members)
[![GitHub stars](https://img.shields.io/github/stars/ujjwalkhandelwal/cso_cuckoo_search_optimization?style=flat-square
)](https://github.com/ujjwalkhandelwal/cso_cuckoo_search_optimization/stargazers)

Implemented fully documented Cuckoo Search Optimization (CSO) algorithm via Levy flights (basic model) using Python. 

## Dependencies
    
  - Numpy
  - matplotlib

## Utilities
Once the installation is finished (download or cloning), go the cso folder and follow the below simple guidelines to execute CSO effectively (either write the code in command line or in a python editor).
```py
>>> from cso import CSO
```
Next, a fitness function (or cost function) is required. I have included **four** different fitness functions for example purposes namely `fitness_1`, `fitness_2`, `fitness_3`, and `fitness_4`.

### Fitness-1 (Himmelblau's Function)
`Minimize:` **f(x) = (x<sup>2</sup> + y - 11)<sup>2</sup> + (x + y<sup>2</sup> - 7)<sup>2</sup>**
    
`Optimum solution`:  ***x = 3 ; y = 2***

### Fitness-2 (Booth's Function)
`Minimize:` **f(x) = (x + 2y - 7)<sup>2</sup> + (2x + y - 5)<sup>2</sup>**

`Optimum solution`:  ***x = 1 ; y = 3***

### Fitness-3 (Beale's Function)
`Minimize:` **f(x) = (1.5 - x - xy)<sup>2</sup> + (2.25 - x + xy<sup>2</sup>)<sup>2</sup> + (2.625 - x + xy<sup>3</sup>)<sup>2</sup>**
    
`Optimum solution`:  ***x = 3 ; y = 0.5***

### Fitness-4
`Maximize:` **f(x) = 2xy + 2x - x<sup>2</sup> - 2y<sup>2</sup>**
    
`Optimum solution`:  ***x = 2 ; y = 1***

```py
>>> from fitness import fitness_1, fitness_2, fitness_3, fitness_4
```

Now, if you want, you can provide bound values for all the particles (not mandatory) and optimize (minimize or maximize) the fitness function using CSO:

**NOTE:** a bool variable `min=True` (default value) for *MINIMIZATION PROBLEM* and `min=False` for *MAXIMIZATION PROBLEM*

```py
>>> CSO(fitness=fitness_1, bound=[(-4,4),(-4,4)]).execute()
```
You will see the following similar output (there can be other minima as well):
```py
OPTIMUM SOLUTION
  > [3.0000078, 1.9999873]

OPTIMUM FITNESS
  > 0.0
```
When **fitness_4** is used, observe that `min=False` since it is a Maximization problem.

```py
>>> CSO(fitness=fitness_4, bound=[(-4,4),(-4,4)], min=False).execute()
```
You will see the following similar output:
```py
OPTIMUM SOLUTION
  > [2.0, 1.0]

OPTIMUM FITNESS
  > 2.0
```

Incase you want to print the fitness value for each iteration, set `verbose=True` (here `Tmax=50` is the 
maximum iteration)

```py
>>> CSO(fitness=fitness_2, Tmax=50, verbose=True).execute()
```
You will see the following similar output:
```py
Iteration:   0  | best global fitness (cost): 18.298822
Iteration:   1  | best global fitness (cost): 1.2203953
Iteration:   2  | best global fitness (cost): 0.8178153
Iteration:   3  | best global fitness (cost): 0.5902262
Iteration:   4  | best global fitness (cost): 0.166928
Iteration:   5  | best global fitness (cost): 0.0926638
Iteration:   6  | best global fitness (cost): 0.0926638
Iteration:   7  | best global fitness (cost): 0.0114517
Iteration:   8  | best global fitness (cost): 0.0114517
Iteration:   9  | best global fitness (cost): 0.0114517
Iteration:   10 | best global fitness (cost): 0.0078867
Iteration:   11 | best global fitness (cost): 0.0078867
Iteration:   12 | best global fitness (cost): 0.0078867
Iteration:   13 | best global fitness (cost): 0.0078867
Iteration:   14 | best global fitness (cost): 0.0069544
Iteration:   15 | best global fitness (cost): 0.0063058
Iteration:   16 | best global fitness (cost): 0.0063058
Iteration:   17 | best global fitness (cost): 0.0011039
Iteration:   18 | best global fitness (cost): 0.0011039
Iteration:   19 | best global fitness (cost): 0.0011039
Iteration:   20 | best global fitness (cost): 0.0011039
Iteration:   21 | best global fitness (cost): 0.0007225
Iteration:   22 | best global fitness (cost): 0.0005875
Iteration:   23 | best global fitness (cost): 0.0001595
Iteration:   24 | best global fitness (cost): 0.0001595
Iteration:   25 | best global fitness (cost): 0.0001595
Iteration:   26 | best global fitness (cost): 0.0001595
Iteration:   27 | best global fitness (cost): 0.0001178
Iteration:   28 | best global fitness (cost): 0.0001178
Iteration:   29 | best global fitness (cost): 0.0001178
Iteration:   30 | best global fitness (cost): 0.0001178
Iteration:   31 | best global fitness (cost): 0.0001178
Iteration:   32 | best global fitness (cost): 0.0001178
Iteration:   33 | best global fitness (cost): 0.0001178
Iteration:   34 | best global fitness (cost): 0.0001178
Iteration:   35 | best global fitness (cost): 0.0001178
Iteration:   36 | best global fitness (cost): 0.0001178
Iteration:   37 | best global fitness (cost): 2.91e-05
Iteration:   38 | best global fitness (cost): 1.12e-05
Iteration:   39 | best global fitness (cost): 1.12e-05
Iteration:   40 | best global fitness (cost): 1.12e-05
Iteration:   41 | best global fitness (cost): 1.12e-05
Iteration:   42 | best global fitness (cost): 1.12e-05
Iteration:   43 | best global fitness (cost): 1.12e-05
Iteration:   44 | best global fitness (cost): 1.12e-05
Iteration:   45 | best global fitness (cost): 1.12e-05
Iteration:   46 | best global fitness (cost): 1.12e-05
Iteration:   47 | best global fitness (cost): 2.4e-06
Iteration:   48 | best global fitness (cost): 2.4e-06
Iteration:   49 | best global fitness (cost): 2.4e-06
Iteration:   50 | best global fitness (cost): 2.4e-06

OPTIMUM SOLUTION
  > [1.0004123, 2.9990281]

OPTIMUM FITNESS
  > 2.4e-06
```

Now, incase you want to plot the fitness value for each iteration, then set `plot=True` (here `Tmax=50` is the 
maximum iteration)

```py
>>> CSO(fitness=fitness_2, Tmax=50, plot=True).execute()
```
You will see the following similar output:
```py
OPTIMUM SOLUTION
  > [1.0028365, 2.9977422]

OPTIMUM FITNESS
  > 1.45e-05
```

![Fitness](https://github.com/ujjwalkhandelwal/pso_particle_swarm_optimization/blob/main/fitness.png)

In case you are interested in implementing **Particle Swarm Optimization** using Python, you can visit [this link!](https://github.com/ujjwalkhandelwal/pso_particle_swarm_optimization) 

### References:    

[1] X. Yang and Suash Deb, "Cuckoo Search via Lévy flights," 2009 World Congress on Nature & Biologically Inspired Computing (NaBIC), 2009, pp. 210-214, doi: 10.1109/NABIC.2009.5393690.

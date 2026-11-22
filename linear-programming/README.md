# Linear Programming Exercise

## Overview

A six-variable linear optimization example using NumPy and SciPy HiGHS to maximize a constrained production profit.

## Academic Objectives

Formulate a constrained production-allocation problem and obtain a numerical solution using linear programming.

## Methodology and Implementation

The script defines six nonnegative decision variables, a linear profit objective, and inequality constraints. Negating the objective converts maximization to the minimization convention used by SciPy; the HiGHS solver computes an allocation.

## Source Organization

- `test.py`: coefficients, constraint matrices, solver call, and printed solution.
- `requirements.txt`: NumPy and SciPy dependencies.

## Environment and Execution

Requirements: Python 3.

```sh
python -m pip install -r requirements.txt
python test.py
```

The script defines the objective, inequality constraints, and nonnegative bounds directly in code and prints the optimal profit and allocations. `test.py` is the application script, not a unit-test file. Associated spreadsheets, figures, and GeoGebra documents were excluded.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

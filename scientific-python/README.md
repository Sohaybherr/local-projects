# Scientific Python Exercises

## Overview

Selected local exercises in plotting, numerical methods, regression, classification, and basic Python object-oriented programming.

## Academic Objectives

Explore numerical computation, graphical analysis, and introductory predictive modelling with Python.

## Methodology and Implementation

Independent scripts use scientific Python libraries for numerical operations, visualization, regression, and classification. Dataset-dependent experiments require their original tabular inputs; the repository does not claim reproduced model performance.

## Source Organization

- `mathplot.py` and related scripts: numerical and visualization exercises.
- `RegreMod.py`: housing regression experiment.
- `ClassMod.py`: weather classification experiment.
- `test.py`: introductory object-oriented exercise.

## Environment and Execution

Requirements: Python 3.

```sh
python -m pip install -r requirements.txt
python mathplot.py
```

Run scripts individually from this directory. `RegreMod.py` expects `housing.csv`; `ClassMod.py` expects `weatherAUS.csv`. Datasets and generated plots were not included, so those examples require separately supplied data. Database loaders, account automation, and unrelated downloaded material were excluded. The selected files are learning experiments rather than a single package.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

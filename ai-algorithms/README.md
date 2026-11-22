# AI Algorithms and Prolog Exercises

## Overview

Python graph-search and machine-learning exercises alongside Prolog knowledge bases and puzzle exercises.

## Academic Objectives

Examine graph traversal, introductory supervised learning, and declarative problem representation.

## Methodology and Implementation

Independent Python scripts express search procedures and machine-learning experiments. Prolog files represent relations and constraints through facts and rules. Some scripts remain exploratory and should be assessed individually.

## Source Organization

- `bfs.py`, `dfs.py`, `dls.py`: search exercises.
- `knn.py` and related scripts: introductory learning experiments.
- `tp2/`, `tp3/`, and `.pl` files: Prolog exercises.

## Environment and Execution

Use Python 3 for `.py` files and SWI-Prolog for `.pl` files.

```sh
python -m pip install -r requirements.txt
python bfs.py
python dfs.py
swipl -s tp3/sudoku.pl
```

`knn.py` expects an `iris.csv` file with a `species` column in the working directory; this dataset was not present locally and is not included. Scripts are independent coursework exercises, including unfinished experiments; installing dependencies does not guarantee every exercise runs.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

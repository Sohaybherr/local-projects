# Java Object-Oriented Programming Exercises

## Overview

Independent Java exercises covering bank accounts, libraries, employees, products, points, geometry, rooms, collections, and vehicles.

## Academic Objectives

Apply encapsulation, inheritance, polymorphism, collections, and exception handling to small domain models.

## Methodology and Implementation

Each directory provides a separate exercise around a concrete domain. Exercises use independent classes and entry points, allowing individual inspection of their design and behavior.

## Source Organization

- Domain directories include banking, library management, employees, geometry, rooms, and vehicles.
- Identical class names may occur across directories; compile each exercise separately.

## Environment and Execution

Requirements: a JDK. Each subdirectory is a separate exercise and should be compiled independently because several exercises reuse class names.

For example, from this directory:

```sh
cd bank
javac *.java
java main
```

Other exercise directories include `bibleo`, `Emp`, `entreprise`, `Facu`, `Marchet1`, `Point`, `PointT`, `Salles`, `Surface`, `Table`, and `Vehicul`. Check each source for its package declaration and entry-point class before running. These exercises do not share a build system or test suite.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

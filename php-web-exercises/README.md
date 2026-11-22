# PHP Student Management Exercises

## Overview

Progressive HTML, CSS, JavaScript, and PHP exercises for student and programme listings, forms, sessions, and database-backed operations.

## Academic Objectives

Examine the progression from static interfaces to server-side forms, session handling, and relational data access.

## Methodology and Implementation

Separate exercises introduce browser interfaces and PHP request processing. Later examples use PDO to query student and programme records in MySQL and session state to manage access.

## Source Organization

- `tp1/`: static web interface exercises.
- `tp3/`–`tp6/`: PHP exercises for listings, forms, sessions, and persistence.
- Connection settings reside in the data-access files of each exercise.

## Environment and Execution

Requirements: PHP; database-backed exercises additionally require MySQL and the PDO MySQL extension.

For example, from this directory:

```sh
php -S localhost:8000 -t tp6
```

Open `http://localhost:8000/accueil.php`. Review `data.php` and equivalent connection code for the selected exercise. The later exercises expect a local `SMI2020` database with tables such as `Etudiant` and `Filiere`; a database dump/schema is not included. `tp1` contains static browser exercises. These examples have not been verified with a live database and are intended for local learning.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

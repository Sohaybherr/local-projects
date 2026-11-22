# Automata and EBNF Scanner Lab

## Overview

A C automaton-minimization exercise and a Java/JFlex scanner for EBNF tokens.

## Academic Objectives

Study finite-state automata and lexical analysis as introductory compilation techniques.

## Methodology and Implementation

A C program implements an automaton-minimization exercise. A separate JFlex specification and Java scanner recognize EBNF token categories, with a driver for inspecting token streams.

## Source Organization

- `comp.c`: automaton exercise.
- `analyse/file.flex`: scanner specification.
- `analyse/EBNFScanner.java`, `EBNFTokens.java`, and `EBNFScannerTest.java`: scanner implementation, token definitions, and driver.

## Environment and Execution

Requirements: a C compiler for `comp.c`, and a JDK for the scanner.

```sh
gcc comp.c -o automata
./automata
cd analyse
javac EBNFTokens.java EBNFScanner.java EBNFScannerTest.java
java EBNFScannerTest test.txt
```

`file.flex` is the scanner specification. Regenerating the scanner requires JFlex; the downloaded JFlex distribution was excluded. Course PDFs, executables, and generated output were excluded. The scanner source is retained as part of the local project.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

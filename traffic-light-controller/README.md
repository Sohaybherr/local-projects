# Arduino Traffic Light Exercise

## Overview

A simple Arduino-style traffic-light sequence using digital outputs 5, 6, and 7.

## Academic Objectives

Represent a timed output sequence using basic embedded control operations.

## Methodology and Implementation

The setup routine initializes digital pins 5, 6, and 7 as outputs. The loop activates these pins sequentially, using delays and repeated pulses to demonstrate a simple traffic-light sequence.

## Source Organization

- `testing/feurouge.c`: Arduino-style source containing `setup()` and `loop()`.

## Environment and Execution

Requirements: an Arduino-compatible board and Arduino IDE/toolchain.

Create an Arduino sketch and copy the contents of `testing/feurouge.c` into its `.ino` file. Connect the outputs according to your board and circuit. The sketch holds output 5 high for 20 seconds, pulses output 6 six times, and holds output 7 high for 15 seconds. The source keeps its original `.c` filename in this archive and is not a standalone desktop C program. Hardware behavior has not been tested.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

# Programming Projects and Academic Exercises

## Overview

This repository brings together fourteen programming projects and practical exercises spanning application development, algorithms, data modelling, scientific computing, and embedded control. Each directory constitutes an independent study with its own implementation requirements and execution procedure.

## Educational Scope

The collection supports the study of software architecture, object-oriented design, declarative programming, data acquisition, relational persistence, formal languages, and numerical optimization. It includes both executable demonstrations and incomplete models retained for examination. No common assessment framework or measured performance comparison is claimed.

## Project Catalogue

| Project | Subject and implementation |
| --- | --- |
| [375Scores Football Dashboard](375scores/README.md) | A React and Vite football interface with an Express/PostgreSQL API for countries, competitions, teams, players, matches, news, search, and user profiles. |
| [AI Algorithms and Prolog Exercises](ai-algorithms/README.md) | Python graph-search and machine-learning exercises alongside Prolog knowledge bases and puzzle exercises. |
| [Electron Chat Demo](electron-chat-demo/README.md) | A small Electron desktop interface that stores message cards locally and returns a fixed placeholder response. |
| [DAAD Degree Programme Scraper](daad-programme-scraper/README.md) | A Python scraper that collects degree-programme information from DAAD and exports JSON and CSV files. |
| [Cote Sport Archive Scraper](cote-sport-archive-scraper/README.md) | A Playwright-based Python utility for collecting archived sports events, odds, and results into local CSV output. |
| [Java Data Group Demo](java-data-group/README.md) | A Java console exercise that adds sample people to a data group, sorts the entries, and displays them. |
| [University Scheduling Model](university-scheduler/README.md) | An unfinished Java model for students, instructors, courses, sections, and time slots, with scheduling utilities. |
| [Java Object-Oriented Programming Exercises](java-oop-exercises/README.md) | Independent Java exercises covering bank accounts, libraries, employees, products, points, geometry, rooms, collections, and vehicles. |
| [XML, DTD, XSD and XSLT Exercises](xml-exercises/README.md) | Markup exercises covering XML documents, DTD and XSD schemas, XSLT stylesheets, and XPath/XQuery examples. |
| [PHP Student Management Exercises](php-web-exercises/README.md) | Progressive HTML, CSS, JavaScript, and PHP exercises for student and programme listings, forms, sessions, and database-backed operations. |
| [Scientific Python Exercises](scientific-python/README.md) | Selected local exercises in plotting, numerical methods, regression, classification, and basic Python object-oriented programming. |
| [Automata and EBNF Scanner Lab](compiler-lab/README.md) | A C automaton-minimization exercise and a Java/JFlex scanner for EBNF tokens. |
| [Arduino Traffic Light Exercise](traffic-light-controller/README.md) | A simple Arduino-style traffic-light sequence using digital outputs 5, 6, and 7. |
| [Linear Programming Exercise](linear-programming/README.md) | A six-variable linear optimization example using NumPy and SciPy HiGHS to maximize a constrained production profit. |

## Repository Organization and Reproduction

Each project README describes its objectives, methodology, source organization, execution environment, and limitations. Select a directory and follow its instructions; the collection has no unified installation or build process. Python requirement files identify direct dependencies without version pins, so they do not define fully reproducible environments. Dataset-dependent examples require separately obtained input data.

## Validation and Interpretation

The [validation report](VALIDATION.md) records the syntax and compiler checks performed. Such checks do not establish end-to-end behavior. External API availability, database integration, model evaluation, and embedded hardware behavior require additional verification in the relevant environment. Incomplete components are identified in the individual project documentation.

## Distribution Notes

The collection contains source material rather than complete execution environments. Generated outputs, dependency directories, executables, private configuration, saved conversations, and unrelated documents are excluded. The football application reads PostgreSQL credentials from environment variables and includes a development API proxy. Database schemas and datasets are not bundled. No repository-wide license has been assigned; existing source notices remain applicable.

## Related Project

The [Weather Forecast Client](https://github.com/Sohaybherr/weather-forecast) is maintained in a separate repository and documents an API-based geocoding and forecast retrieval workflow.

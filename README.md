# Local Projects

A collection of my local programming projects and university exercises, organized by topic. Each project has its own README with prerequisites, usage, and known limitations.

## Projects

| Project | Description |
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

## Getting started

Clone this repository, choose a project, and follow its README. Projects are independent; there is no shared install command or unified build. Python dependency files list direct packages without pinning versions because the original projects did not provide reproducible environments.

## About this collection

This is a source snapshot of local work, including unfinished coursework. Dependencies, archives, executables, saved chats, private environment files, downloaded datasets, and unrelated personal documents were excluded. Existing portfolio repositories and a portfolio linked to another GitHub account were not duplicated. Original local folders were left unchanged.

The publication copy of 375Scores uses PostgreSQL environment variables instead of a hardcoded password and adds a Vite development API proxy. Runtime database schemas and data are not bundled. No live scraping, database integration, or Arduino hardware tests were performed.

See [VALIDATION.md](VALIDATION.md) for checks and existing source issues. No license has been added; retain any notices in the individual source files.

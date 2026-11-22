# Automata and EBNF Scanner Lab

A C automaton-minimization exercise and a Java/JFlex scanner for EBNF tokens.

## Usage

Requirements: a C compiler for `comp.c`, and a JDK for the scanner.

```sh
gcc comp.c -o automata
./automata
cd analyse
javac EBNFTokens.java EBNFScanner.java EBNFScannerTest.java
java EBNFScannerTest test.txt
```

`file.flex` is the scanner specification. Regenerating the scanner requires JFlex; the downloaded JFlex distribution was excluded. Course PDFs, executables, and generated output were excluded. The scanner source is retained as part of the local project.

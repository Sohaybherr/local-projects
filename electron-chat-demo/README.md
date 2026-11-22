# Electron Chat Demo

## Overview

A small Electron desktop interface that stores message cards locally and returns a fixed placeholder response.

## Academic Objectives

Investigate event-driven desktop interfaces and local persistence using Electron.

## Methodology and Implementation

The main process creates a browser window. The renderer constructs message cards, handles submission events, and serializes conversation state to JSON. Responses are generated from a fixed string template.

## Source Organization

- `app.js`: Electron application lifecycle.
- `main.js`: interaction and persistence logic.
- `index.html`: interface entry document.

## Environment and Execution

Requirements: Node.js/npm and a desktop environment.

```sh
npm ci
npm start
```

`app.js` opens the window; `main.js` handles rendering and persistence. `save.json` is created when needed and is ignored by Git. Existing conversation history was excluded. The response is a template string; no AI model or API is connected. This local prototype enables Node integration in the renderer and has not been packaged or hardened for distribution.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.

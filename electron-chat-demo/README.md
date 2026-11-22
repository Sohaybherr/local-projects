# Electron Chat Demo

A small Electron desktop interface that stores message cards locally and returns a fixed placeholder response.

## Usage

Requirements: Node.js/npm and a desktop environment.

```sh
npm ci
npm start
```

`app.js` opens the window; `main.js` handles rendering and persistence. `save.json` is created when needed and is ignored by Git. Existing conversation history was excluded. The response is a template string; no AI model or API is connected. This local prototype enables Node integration in the renderer and has not been packaged or hardened for distribution.

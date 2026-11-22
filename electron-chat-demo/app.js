const { app, BrowserWindow, Menu } = require('electron');

function createWindow() {
  const win = new BrowserWindow({
    width: 600,
    height: 400,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });


  Menu.setApplicationMenu(null);

  win.loadFile('index.html');
}

app.whenReady().then(createWindow);

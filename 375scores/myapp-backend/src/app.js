const express = require("express");
const path = require("path");

const countriesRoutes = require("./modules/countries/countries.routes");
const competitionsRoutes = require("./modules/competitions/competitions.routes");
const teamsRoutes = require("./modules/teams/teams.routes");
const playersRoutes = require("./modules/players/players.routes");
const matchesRoutes = require("./modules/matches/matches.routes");
const newsRoutes = require("./modules/news/news.routes");
const usersRoutes = require("./modules/users/users.routes");
const homeRoutes = require("./modules/home/home.routes");
const searchRoutes = require("./modules/search/search.routes");

const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.send("Backend is running...");
});

app.get("/tester", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "api-tester.html"));
});

app.use("/api/v1/home", homeRoutes);
app.use("/api/v1/search", searchRoutes);
app.use("/api/v1/countries", countriesRoutes);
app.use("/api/v1/competitions", competitionsRoutes);
app.use("/api/v1/teams", teamsRoutes);
app.use("/api/v1/players", playersRoutes);
app.use("/api/v1/matches", matchesRoutes);
app.use("/api/v1/news", newsRoutes);
app.use("/api/v1/users", usersRoutes);

module.exports = app;

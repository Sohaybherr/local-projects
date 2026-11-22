const express = require("express");
const teamsController = require("./teams.controller");

const router = express.Router();

router.get("/", teamsController.getAllTeams);
router.get("/api/:apiId", teamsController.getTeamByApiId);
router.get("/country/:countryId", teamsController.getTeamsByCountry);
router.get("/name/:name", teamsController.getTeamsByName);
router.get("/competition/:competitionId/season/:seasonId", teamsController.getTeamsByCompetitionAndSeason);
router.get("/:teamId/competitions/season/:seasonId", teamsController.getCompetitionsByTeamAndSeason);
router.get("/:id/details", teamsController.getTeamDetails);
router.get("/:id", teamsController.getTeamById);

module.exports = router;

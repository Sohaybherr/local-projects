const express = require("express");
const matchesController = require("./matches.controller");

const router = express.Router();

router.get("/", matchesController.getAllMatches);
router.get("/competition/:competitionId/season/:seasonId", matchesController.getMatchesByCompetitionAndSeason);
router.get("/competition/:competitionId/date-range", matchesController.getMatchesByDateRangeAndCompetition);
router.get(
  "/team/:teamId/season/:seasonId/competition/:competitionId",
  matchesController.getMatchesByTeamAndSeasonAndCompetition
);
router.get("/:id/details", matchesController.getMatchDetails);
router.get("/:id", matchesController.getMatchById);

module.exports = router;

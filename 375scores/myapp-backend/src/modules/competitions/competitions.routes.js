const express = require("express");
const competitionsController = require("./competitions.controller");

const router = express.Router();

router.get("/", competitionsController.getAllCompetitions);
router.get("/country/:country", competitionsController.getCompetitionsByCountry);
router.get("/:id/seasons/:seasonId/details", competitionsController.getCompetitionDetails);
router.get("/:id/details", competitionsController.getCompetitionDetails);
router.get("/:id/type", competitionsController.getCompetitionType);
router.get("/:id", competitionsController.getCompetitionById);

module.exports = router;

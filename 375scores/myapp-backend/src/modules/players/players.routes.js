const express = require("express");
const playersController = require("./players.controller");

const router = express.Router();

router.get("/", playersController.getAllPlayers);
router.get("/api/:apiId", playersController.getPlayerByApiId);
router.get("/country/:countryId", playersController.getPlayersByCountry);
router.get("/team/:teamId", playersController.getPlayersByTeam);
router.get("/position/:position", playersController.getPlayersByPosition);
router.get("/name/:name", playersController.getPlayersByName);
router.get("/:id/details", playersController.getPlayerDetails);
router.get("/:id", playersController.getPlayerById);

module.exports = router;

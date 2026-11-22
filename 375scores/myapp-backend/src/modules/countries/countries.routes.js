const express = require("express");
const countriesController = require("./countries.controller");

const router = express.Router();

router.get("/", countriesController.getAllCountries);
router.get("/name/:name", countriesController.getCountryByName);
router.get("/:id", countriesController.getCountryById);

module.exports = router;

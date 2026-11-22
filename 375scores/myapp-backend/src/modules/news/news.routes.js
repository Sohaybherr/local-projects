const express = require("express");
const newsController = require("./news.controller");

const router = express.Router();

router.get("/", newsController.getAllNews);
router.post("/", newsController.createNews);
router.get("/latest", newsController.getLatestNews);
router.get("/:id", newsController.getNewsById);
router.put("/:id", newsController.updateNews);
router.delete("/:id", newsController.deleteNews);

module.exports = router;

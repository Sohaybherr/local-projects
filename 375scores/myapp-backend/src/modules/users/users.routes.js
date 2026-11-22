const express = require("express");
const usersController = require("./users.controller");

const router = express.Router();

router.get("/", usersController.getAllUsers);
router.post("/", usersController.createUser);
router.post("/login", usersController.loginUser);
router.get("/username/:username", usersController.getUserByUsername);
router.get("/email/:email", usersController.getUserByEmail);
router.get("/:id/profile", usersController.getUserProfile);
router.get("/:id", usersController.getUserById);
router.put("/:id", usersController.updateUser);
router.delete("/:id", usersController.deleteUser);

module.exports = router;

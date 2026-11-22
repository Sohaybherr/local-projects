const usersModel = require("./users.model");

function handleUniqueViolation(error, res) {
  if (error.code !== "23505") {
    return false;
  }

  if (error.constraint && error.constraint.includes("username")) {
    res.status(409).json({ error: "Username already exists" });
    return true;
  }

  if (error.constraint && error.constraint.includes("email")) {
    res.status(409).json({ error: "Email already exists" });
    return true;
  }

  res.status(409).json({ error: "User already exists" });
  return true;
}

async function getAllUsers(req, res) {
  try {
    const users = await usersModel.getAllUsers();
    res.json(users);
  } catch (error) {
    console.error("Error fetching users:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getUserById(req, res) {
  const { id } = req.params;

  try {
    const user = await usersModel.getUserById(id);

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json(user);
  } catch (error) {
    console.error("Error fetching user:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getUserByUsername(req, res) {
  const { username } = req.params;

  try {
    const user = await usersModel.getUserByUsername(username);

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json(user);
  } catch (error) {
    console.error("Error fetching user by username:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getUserByEmail(req, res) {
  const { email } = req.params;

  try {
    const user = await usersModel.getUserByEmail(email);

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json(user);
  } catch (error) {
    console.error("Error fetching user by email:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function createUser(req, res) {
  const { username, email, password, profilePicture } = req.body;

  if (!username || !email || !password) {
    return res.status(400).json({ error: "username, email, and password are required" });
  }

  try {
    const user = await usersModel.createUser({ username, email, password, profilePicture });
    res.status(201).json(user);
  } catch (error) {
    if (handleUniqueViolation(error, res)) {
      return;
    }

    console.error("Error creating user:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function loginUser(req, res) {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: "email and password are required" });
  }

  try {
    const user = await usersModel.getUserByEmailWithPassword(email);

    if (!user || user.password !== password) {
      return res.status(401).json({ error: "Invalid email or password" });
    }

    delete user.password;
    res.json(user);
  } catch (error) {
    console.error("Error logging in user:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function updateUser(req, res) {
  const { id } = req.params;
  const { username, email, password, profilePicture } = req.body;

  try {
    const user = await usersModel.updateUser(id, { username, email, password, profilePicture });

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json(user);
  } catch (error) {
    if (handleUniqueViolation(error, res)) {
      return;
    }

    console.error("Error updating user:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function deleteUser(req, res) {
  const { id } = req.params;

  try {
    const user = await usersModel.deleteUser(id);

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json(user);
  } catch (error) {
    console.error("Error deleting user:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getUserProfile(req, res) {
  const { id } = req.params;

  try {
    const profile = await usersModel.getUserById(id);

    if (!profile) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json({
      profile,
      favoriteTeams: [],
      favoritePlayers: [],
      favoriteCompetitions: []
    });
  } catch (error) {
    console.error("Error fetching user profile:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

module.exports = {
  getAllUsers,
  getUserById,
  getUserByUsername,
  getUserByEmail,
  createUser,
  loginUser,
  updateUser,
  deleteUser,
  getUserProfile
};

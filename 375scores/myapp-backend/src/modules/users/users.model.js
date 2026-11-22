const pool = require("../../config/db");

const publicUserFields = "id, username, email, profile_picture, created_at, updated_at";

async function getAllUsers() {
  const result = await pool.query(`SELECT ${publicUserFields} FROM users`);
  return result.rows;
}

async function getUserById(id) {
  const result = await pool.query(`SELECT ${publicUserFields} FROM users WHERE id = $1`, [id]);
  return result.rows[0];
}

async function getUserByUsername(username) {
  const result = await pool.query(`SELECT ${publicUserFields} FROM users WHERE username = $1`, [username]);
  return result.rows[0];
}

async function getUserByEmail(email) {
  const result = await pool.query(`SELECT ${publicUserFields} FROM users WHERE email = $1`, [email]);
  return result.rows[0];
}

async function getUserByEmailWithPassword(email) {
  const result = await pool.query(
    `SELECT ${publicUserFields}, password FROM users WHERE email = $1`,
    [email]
  );
  return result.rows[0];
}

async function createUser(user) {
  const { username, email, password, profilePicture } = user;
  const query = `
    INSERT INTO users (username, email, password, profile_picture)
    VALUES ($1, $2, $3, $4)
    RETURNING ${publicUserFields}
  `;
  const result = await pool.query(query, [username, email, password, profilePicture || null]);
  return result.rows[0];
}

async function updateUser(id, user) {
  const { username, email, password, profilePicture } = user;
  const query = `
    UPDATE users
    SET
      username = COALESCE($1, username),
      email = COALESCE($2, email),
      password = COALESCE($3, password),
      profile_picture = COALESCE($4, profile_picture),
      updated_at = CURRENT_TIMESTAMP
    WHERE id = $5
    RETURNING ${publicUserFields}
  `;
  const result = await pool.query(query, [username, email, password, profilePicture, id]);
  return result.rows[0];
}

async function deleteUser(id) {
  const result = await pool.query(`DELETE FROM users WHERE id = $1 RETURNING ${publicUserFields}`, [id]);
  return result.rows[0];
}

module.exports = {
  getAllUsers,
  getUserById,
  getUserByUsername,
  getUserByEmail,
  getUserByEmailWithPassword,
  createUser,
  updateUser,
  deleteUser
};

const pool = require("../../config/db");

async function getAllPlayers() {
  const result = await pool.query("SELECT * FROM players");
  return result.rows;
}

async function getPlayerById(id) {
  const result = await pool.query("SELECT * FROM players WHERE id = $1", [id]);
  return result.rows[0];
}

async function getPlayerByApiId(apiId) {
  const result = await pool.query("SELECT * FROM players WHERE api_id = $1", [apiId]);
  return result.rows[0];
}

async function getPlayersByCountry(countryId) {
  const result = await pool.query("SELECT * FROM players WHERE country_id = $1", [countryId]);
  return result.rows;
}

async function getPlayersByTeam(teamId) {
  const result = await pool.query("SELECT * FROM players WHERE current_team_id = $1", [teamId]);
  return result.rows;
}

async function getPlayersByPosition(position) {
  const result = await pool.query("SELECT * FROM players WHERE position ILIKE $1", [position]);
  return result.rows;
}

async function getPlayersByName(name) {
  const result = await pool.query("SELECT * FROM players WHERE full_name ILIKE $1", [`%${name}%`]);
  return result.rows;
}

module.exports = {
  getAllPlayers,
  getPlayerById,
  getPlayerByApiId,
  getPlayersByCountry,
  getPlayersByTeam,
  getPlayersByPosition,
  getPlayersByName
};

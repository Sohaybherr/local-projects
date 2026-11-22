const pool = require("../../config/db");

async function getAllTeams() {
  const result = await pool.query("SELECT * FROM teams");
  return result.rows;
}

async function getTeamById(id) {
  const result = await pool.query("SELECT * FROM teams WHERE id = $1", [id]);
  return result.rows[0];
}

async function getTeamByApiId(apiId) {
  const result = await pool.query("SELECT * FROM teams WHERE api_id = $1", [apiId]);
  return result.rows[0];
}

async function getTeamsByCountry(countryId) {
  const result = await pool.query("SELECT * FROM teams WHERE country_id = $1", [countryId]);
  return result.rows;
}

async function getTeamsByName(name) {
  const result = await pool.query("SELECT * FROM teams WHERE name ILIKE $1", [`%${name}%`]);
  return result.rows;
}

async function getTeamsByCompetitionAndSeason(competitionId, seasonId) {
  const query = `
    SELECT teams.*
    FROM teams
    INNER JOIN team_competitions
      ON team_competitions.team_id = teams.id
    WHERE team_competitions.competition_id = $1
      AND team_competitions.season_id = $2
  `;
  const result = await pool.query(query, [competitionId, seasonId]);
  return result.rows;
}

async function getCompetitionsByTeamAndSeason(teamId, seasonId) {
  const query = `
    SELECT competitions.*
    FROM competitions
    INNER JOIN team_competitions
      ON team_competitions.competition_id = competitions.id
    WHERE team_competitions.team_id = $1
      AND team_competitions.season_id = $2
  `;
  const result = await pool.query(query, [teamId, seasonId]);
  return result.rows;
}

module.exports = {
  getAllTeams,
  getTeamById,
  getTeamByApiId,
  getTeamsByCountry,
  getTeamsByName,
  getTeamsByCompetitionAndSeason,
  getCompetitionsByTeamAndSeason
};

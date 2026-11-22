const pool = require('../../config/db');

async function getAllMatches() {
  const query = 'SELECT * FROM matches';
  const result = await pool.query(query);
  return result.rows;
}
async function getMatchById(id) {
  const query = 'SELECT * FROM matches WHERE id = $1';
  const result = await pool.query(query, [id]);
  return result.rows[0];
}
async function getMatchesByCompetitionAndSeason(competitionId, seasonId) {
  const query = 'SELECT * FROM matches WHERE competition_id = $1 AND season_id = $2';
  const result = await pool.query(query, [competitionId, seasonId]);
  return result.rows;
}
async function getMatchesByTeamAndSeasonAndCompetition(teamId, seasonId, competitionId) {
  const query = 'SELECT * FROM matches WHERE (home_team = $1 OR away_team = $1) AND season_id = $2 AND competition_id = $3';
  const result = await pool.query(query, [teamId, seasonId, competitionId]);
  return result.rows;
}
async function getMatchesByDateRangeAndCompetition(startDate, endDate, competitionId) {
  const query = 'SELECT * FROM matches WHERE match_date BETWEEN $1 AND $2 AND competition_id = $3';
  const result = await pool.query(query, [startDate, endDate, competitionId]);
  return result.rows;
}

module.exports = {
  getAllMatches,
  getMatchById,
  getMatchesByCompetitionAndSeason,
  getMatchesByTeamAndSeasonAndCompetition,
  getMatchesByDateRangeAndCompetition
};
